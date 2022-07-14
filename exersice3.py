# В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

# lesson – начало и конец урока
# pupil – интервалы присутствия ученика
# tutor – интервалы присутствия учителя
# Интервалы устроены следующим образом – это всегда список из четного количества элементов. 
# Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
# Нужно написать функцию, которая получает на вход словарь с интервалами 
# и возвращает время общего присутствия ученика и учителя на уроке (в секундах).


def ret_min_max(val1, val2):
    if len(val1) > len(val2):
        return val2, val1
    return val1, val2


def appearance(intervals: dict) -> int:
    limit = intervals["lesson"]
    sub_limit, main_intervals = ret_min_max(intervals["pupil"], intervals["tutor"])
    print(len(sub_limit), len(main_intervals))




    total_time = 0
    for i in range(0, len(sub_limit), 2):
        if sub_limit[i] <= limit[0]:
            sub_limit[i] = limit[0]
        if sub_limit[i+1] >= limit[1]:
            sub_limit[i+1] = limit[1]

        for j in range(0, len(main_intervals), 2):
            if main_intervals[j] <= limit[0]:
                main_intervals[j] = limit[0]
            if main_intervals[j+1] >= limit[1]:
                main_intervals[j+1] = limit[1]

            if main_intervals[j+1] <= sub_limit[i]:
                continue
            if main_intervals[j] >= sub_limit[i+1]:
                break

            if sub_limit[i] <= main_intervals[j] and main_intervals[j+1] <= sub_limit[i+1]:
                total_time += main_intervals[j+1] - main_intervals[j]
            elif main_intervals[j+1] >= sub_limit[i+1] and main_intervals[j] <= sub_limit[i+1]:
                total_time += sub_limit[i+1] - main_intervals[j]
            elif sub_limit[i] <= main_intervals[j+1] <= sub_limit[i+1]:
                total_time += main_intervals[j+1] - sub_limit[i]
    

    return total_time


tests = [
    {"data": {"lesson": [1594663200, 1594666800],
             "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             "tutor": [1594663290, 1594663430, 1594663443, 1594666473]},
     "answer": 3117
    },
    {"data": {"lesson": [1594702800, 1594706400],
             "pupil": [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             "tutor": [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    "answer": 3577
    },
    {"data": {"lesson": [1594692000, 1594695600],
             "pupil": [1594692033, 1594696347],
             "tutor": [1594692017, 1594692066, 1594692068, 1594696341]},
    "answer": 3565
    },
]

if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["data"])
        assert test_answer == test["answer"], f"Error on test case {i}, got {test_answer}, expected {test['answer']}"

    print("TASK DONE!")
