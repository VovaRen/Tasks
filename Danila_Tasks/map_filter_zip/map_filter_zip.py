from functools import reduce

# есть два списка
test_1 = [1, 2, 3, 4, 5, 6]
test_2 = [3, 4, 5, 6, 7, 8]


# 1 написать мап функцию- с использование лямбда-выражения для умножения кадго значения  test_1 на 2 в 1 строку
def multiplication_test_1(test_1):
    """Функция умножает каждый элемент списка
    на 2.
    :param test_1: list
    """
    print(list(map(lambda x: x * 2, test_1)))


# 2 через функцию map перемножить test_1 и test_2 поэлементно в 1 строку
def multiplication(test_1, test_2):
    """Функция поэлементно перемножает
    2 списка.
    :param test_1: list
    :param test_2: list
    """
    print(list(map(lambda x, y: x * y, test_1, test_2)))


# 3 через функцию filter вернуть все элементы test_2 которые делятся целочисленно на 3
def filter_test_2(test_2):
    """Возвращает все элементы списка кратные 3.
    :param test_2: list
    """
    print(list(filter(lambda x: x % 3 == 0, test_2)))


# 4 через функцию reduce вернуть cумму всех элементов списка test1 + test2 (должно получиться 54)
def sum_tests(test_1, test_2):
    """Возвращает сумму всех элементов
    списка test_1 + test_2.
    :param test_1: list
    :param test_2: list
    """
    sum_test = reduce(lambda x, y: x + y, test_1 + test_2)
    print(sum_test)


# 5 через zip объеденить оба списка
def zip_tests(test_1, test_2):
    """Функция объеденяет 2 списка.
    :param test_1: list
    :param test_2: list
    """
    print(list(zip(test_1, test_2)))


if __name__ == '__main__':
    multiplication_test_1(test_1)
    multiplication(test_1, test_2)
    filter_test_2(test_2)
    sum_tests(test_1, test_2)
    zip_tests(test_1, test_2)
