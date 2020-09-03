# A.Нужно сложить два словаря и получить один.
def sum_dicts(dict_1, dict_2):
    """Функция складывает 2 списка.
    :param dict_1: dict
    :param dict_2: dict
    :return two_dicts: dict
    """
    two_dicts = {**dict_1, **dict_2}
    return two_dicts


# Б.Найти в списке словарей нужный словарь.
def search_dict(list, dict):
    """Функция ищет вхождение словаря
    в словарях, находящихся в списке.
    :param list: list
    :param dict: dict
    :return search_dict: str
    """
    for x in list:
        for item in x:
            if item in dict and x[item] == dict[item]:
                return 'Словарь есть в списке'
            else:
                return 'Словаря нет в списке'


# В.Найти сумму всех четных чисел ряда Фибоначи  < 4000000
def sum_fib(lim):
    """Возвращает сумму четных чисел
    Фибоначчи < 4000000.
    :param lim:
    :return sum(x): int
    """
    fib =[0, 1]
    ind = 1
    h = 0
    while h < lim:
        ind += 1
        z = fib[ind-2] + fib[ind-1]
        if z < lim:
            fib.append(z)
            x = [i for i in fib if i%2 == 0]
            h = max(x)
        else:
            break
    return sum(x)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('Сложение словарей:')
    test(sum_dicts({1: 'Hello', 2: 'my'}, {3: 'dear', 4: 'friend'}), {1: 'Hello', 2: 'my', 3: 'dear', 4: 'friend'})

    print()
    print('Наличие словаря в списке:')
    test(search_dict([{'EDType': 'C101', 'a': 2}, {'EDType': 'C102', 'b': 3}], {'EDType': 'C101'}), 'Словарь есть в списке')
    test(search_dict([{'EDType': 'C101', 'a': 2}, {'EDType': 'C102', 'b': 3}], {'EDType': 'C103'}), 'Словаря нет в списке')

    print()
    print('Сумма четных Фибоначчи:')
    test(sum_fib(4000000), 4613732)

if __name__ == '__main__':
    main()


