from animals import animals
from config import *


# примечание: max_points всегда должно быть большее на балл, чем сумма всех баллов!!!
max_points = 21

if question_2:
    max_points += 20
if question_3:
    max_points += 20
if question_4:
    max_points += 20
if question_5:
    max_points += 20
if question_6:
    max_points += 20
if question_7:
    max_points += 20
if question_8:
    max_points += 20
if question_9:
    max_points += 20
if question_10:
    max_points += 20

# Функция, которая принимает путь к нужной папке и выдает количество элементов в ней
def len_dict(my_dict, keys):
    for k, v in my_dict.items():
        if k == keys[0]:
            val1 = v
            for k1, v1 in val1.items():
                if type(k1) is int:
                    return len(v)
            else:
                for k1, v1 in val1.items():
                    if k1 == keys[1]:
                        val2 = v1
                        for k2, v2 in val2.items():
                            if type(k2) is int:
                                return len(v1)
                        else:
                            for k2, v2 in val2.items():
                                if k2 == keys[2]:
                                    val3 = v2
                                    for k3, v3 in val3.items():
                                        if type(k3) is int:
                                            return len(v2)
                                    else:
                                        for k3, v3 in val3.items():
                                            if k3 == keys[3]:
                                                return len(v3)


#counter = 0
# Функция, которая формирует позицию на основании баллов и количества элементов всего и
# формирует ключ, объединяя позицию и путь
def create_key(points=int, code=list):
    value2 = len_dict(animals, code)
    value = max_points / value2
    value1 = [int(points / value + 1)]
    value3 = code + value1
    return value3


# Функция, которая вытаскивает нужный элемент с массива
def get_key(my_dict, point, code):
    keys = create_key(point, code)
    for k, v in my_dict.items():
        if k == keys[0]:
            val = v
            for k, v in val.items():
                if k == keys[1] and type(k) is int:
                    return v
            else:
                for k, v in val.items():
                    if k == keys[1]:
                        val = v
                        for k, v in val.items():
                            if k == keys[2] and type(k) is int:
                                return v
                        else:
                            for k, v in val.items():
                                if k == keys[2]:
                                    val = v
                                    for k, v in val.items():
                                        if k == keys[3] and type(k) is int:
                                            return v
                                    else:
                                        for k, v in val.items():
                                            if k == keys[3]:
                                                val = v
                                                for k, v in val.items():
                                                    if k == keys[4]:
                                                        return v

