# Задача №1.
# Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, 
# за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
# Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)


def task(array: str) -> int:
    if "0" in array.strip(" "):
        array = array.replace(" ", "")
        return array.index("0")
    else:
        return "Not found"


if __name__ == "__main__":
    values = input("Enter array of numbers without spaces:\n")

    print(task(values))
