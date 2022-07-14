# Задача №2.
# В нашей школе мы не можем разглашать персональные данные пользователей, 
# но чтобы преподаватель и ученик смогли объяснить нашей поддержке, 
# кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), 
# мы генерируем пользователям уникальные и легко произносимые имена. 
# Имя у нас состоит из прилагательного, имени животного и двузначной цифры. 
# В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
# Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) 
# и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
# А: 642
# Б: 412

import requests as req
from bs4 import BeautifulSoup
from string import ascii_uppercase
import json
from clock import log_time, Timer


@log_time
def get_html(url: str):
    response = req.get(url)
    if response.ok:
        return response.text
    else:
        return print(response.status_code)


@log_time
def get_data(page: str) -> list:
    html = BeautifulSoup(page, "lxml")
    main_div = html.find("div", id="mw-pages")
    animals = main_div.find_all("div", class_="mw-category-group")
    next_link = main_div.find("a", string="Следующая страница").get("href")
    return animals, next_link


def count_first_letter(value: str, result: dict):
    if value not in result.keys():
        result.setdefault(value.upper(), 1)
    else:
        result[value.upper()] += 1


@log_time
def process_data(data: list, result: dict) -> bool:
    for group in data:
        if group.find("h3").text.upper() in ascii_uppercase:
            return True

        list_items = set(map(lambda li: li.text.split(" (")[0], group.find_all("li")))
        for animal in list_items:
            if set(ascii_uppercase).intersection(set(animal.upper())):
                continue
            
            count_first_letter(animal[0], result)

    return False
    

@log_time
def to_json(data, file_name) -> None:
    with open(f"./{file_name}.json", "wt", encoding="utf-8") as _file:
        json.dump(data, _file, ensure_ascii=False)


@log_time
def main(*args, **kwargs) -> None:
    result = dict()
    url = r"https://ru.wikipedia.org"
    next_link = r"/w/index.php?title=Категория:Животные_по_алфавиту"
    stop = False
    while not stop:
        current_url = url + next_link

        data, next_link = get_data(get_html(current_url))

        stop = process_data(data, result)


    to_json(result, "answer")
    print("Parsing END!")


if __name__ == "__main__":
    Timer.set_file("wiki_pars.txt")
    main()
