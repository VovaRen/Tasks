#!/usr/bin/python3

"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее 
часто встречающихся слов, таким образом первым будет самое часто встречающееся 
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import string
import sys

WORDS_IN_TEXT = []
ALL_WORDS = []


# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.
def read_text(filename):
    """
    Функция форматирует текст и возвращает
    все слова в тексте в виде списка, а
    так же уникальные слова в этом
    списке в виде множества.
    :param filename:
    :return words_set: set
    :return words: list
    """
    global WORDS_IN_TEXT
    global ALL_WORDS
    with open(filename) as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    ALL_WORDS = text.split()
    ALL_WORDS.sort()
    WORDS_IN_TEXT = set(ALL_WORDS)
    return WORDS_IN_TEXT, ALL_WORDS


def print_words(filename):
    """
    Функция печатает слова и их
    кол-во в тексте.
    :param filename:
    :return:
    """
    read_text(filename)
    for i in WORDS_IN_TEXT:
        words_in_list = ALL_WORDS.count(i)
        print(f'{i}: {words_in_list}')


def print_top(filename):
    """
    Функция печатает 20 наиболее
    встречающихся слов в тексте
    и их кол-во.
    :param filename:
    :return:
    """
    read_text(filename)
    top_values = {}
    for i in WORDS_IN_TEXT:
        words_in_list = ALL_WORDS.count(i)
        top_values[i] = words_in_list
    items_top_values = list(top_values.items())
    items_top_values.sort(key=lambda x: x[1], reverse=True)
    for i in items_top_values[:20]:
        print(i[0], ':', i[1])


###


# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.
def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)


if __name__ == '__main__':
    main()
