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
def search_dict(dicts_list, dict_in_list):
    """Функция ищет вхождение словаря
    в словарях, находящихся в списке.
    :param dicts_list: list
    :param dict_in_list: dict
    :return search_dict: str
    """
    presence = 0
    for element in dicts_list:
        if element == dict_in_list:
            presence += 1
    if presence > 0:
        return 'Словарь есть в списке'
    else:
        return 'Словаря нет в списке'


# В.Найти сумму всех четных чисел ряда Фибоначи  < 4000000
def sum_fib():
    """Возвращает сумму четных чисел
    Фибоначчи < 4000000.
    :param:
    :return sum_even: int
    """
    sum_even = 0
    fib_1, fib_2 = 0, 1
    while fib_1 <= 4000000:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        if fib_1 % 2:
            continue
        sum_even += fib_1
    return sum_even


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
    test(search_dict([{'EDType': 'C101', 'a': 2}, {'EDType': 'C102', 'b': 3}], {'EDType': 'C102', 'b': 3}),
         'Словарь есть в списке')
    test(search_dict([{'EDType': 'C101', 'a': 2}, {'EDType': 'C102', 'b': 3}], {'EDTyp': 'C103', 'EDType': 'C101'}),
         'Словаря нет в списке')

    print()
    print('Сумма четных Фибоначчи:')
    test(sum_fib(), 4613732)


if __name__ == '__main__':
    main()
