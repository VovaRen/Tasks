import time
import sys


def func_info(func):
    def info(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        print('Название функции:', func.__name__)
        print('Размер функции:', sys.getsizeof(func))
        print(f'Время работы функции: {end_time - start_time} сек.')
        print('Функция возвращает:', result)
    return info


@func_info
def qwe(q, w, e):
    print('TEST')
    c = (q + w + e + 10 + 1525648954654 + 5648954654*3)/26256462123546 * 5164654684564655123
    return c


if __name__ == '__main__':
    qwe(1, 2, 1000)
