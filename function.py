from animals import animals


# примечание: max_points всегда должно быть выше на балл чем сумма всех баллов!!!
max_points = 101


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


# name = 'vlad'
#
# users = {}
# users[name] = {}
# users[name]['rez'] = []
# users[name]['id'] = ''
# users[name]['rez'].append('koko')
# users[name]['rez'].append('momo')
#
# print(users)
# print(users[name]['rez'][2])

#test
# my_point = 100
#
# test1 = 'bats'
# test2 = ['plain_dune', 'herbivores', 'birds', 'cancerous']
# test3 = ['wood_jungles', 'predatory', 'cats']
# test4 = ['plain_dune', 'herbivores', 'birds', 'chicken']
# test5 = ['swamp', 'crocodile']


# print(get_key(animals, my_point, test1))
# print(get_key(animals, my_point, test2))
# print(get_key(animals, my_point, test3))
# print(get_key(animals, my_point, test4))
# print(get_key(animals, my_point, test5))


# print(animals[test1])
# print(len(animals[test1]))
# print(animals[test2])
# print(len(animals[test2]))
# print(len(animals['mount']['predatory']['cats']))
# print(animals['mount']['predatory']['cats'][2])

# rez = Image.open(get_key(val, k1))
# rez1 = Image.open(get_key(val, k))
#
#
# rez1.show()
# rez.show()