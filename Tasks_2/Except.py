# Функция принимает числа введённые пользователем
# через пробел.
# Необходимо вернуть их сумму, если
# все элементы являются чилами и их
# кол-во меньше 11.
# Если какое-то из условий не соблюдается
# вызвать исключение.
def sum_nums():
    """Функция складывает не более 10 целых
    чисел (чисел с плавающей точкой), введенных пользователем.
    :return sum_nums: float
    """
    input_nums = input("Введите несколько чисел через пробел (не больше 10): ")
    try:
        list_input_nums = [float(i) for i in input_nums.split(' ')]
        if len(list_input_nums) < 11:
            print("Сумма введённых чисел: ", sum(list_input_nums))
        else:
            raise ValueError
    except ValueError:
        print('Введите только числа через пробел в кол-ве не больше 10!')
        sum_nums()


if __name__ == '__main__':
    sum_nums()
