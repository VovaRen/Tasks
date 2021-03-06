import time
from threading import Thread
from functools import partial, reduce, wraps
from typing import Callable, Iterable, Union, AnyStr, TypeVar, Tuple, Mapping, Dict

T = TypeVar('T')


# Флет
def flat(test_list: Iterable[T]) -> T:
    for elem in test_list:
        if isinstance(elem, Iterable) and not isinstance(elem, (str, bytes)):
            yield from flat(elem)
        else:
            yield elem


# Декоратор для функции
def func_info(func: Callable[[T], T]) -> Callable[[T], T]:
    @wraps(func)
    def info(*args: Tuple[any], **kwargs: Mapping[str, any]):
        # Если точка присутствует, то функция является методом
        if '.' in func.__qualname__:
            print(func.__name__)
        thread = Thread(target=partial(func, *args, **kwargs), daemon=True)
        thread.start()
        thread.join(2)
    return info


# Декаориуемая функция (time.sleep для проверки)
@func_info
def time_sleeper(sec: int) -> None:
    time.sleep(sec)
    print('Я выполнилась!')


# Чейн 1 версия
def chain_1(this_is_text: T, *args: Callable[[T], T]) -> T:
    result: T = this_is_text
    for func in args:
        result: T = func(result)
    return result


# Чейн 2 версия
def chain_2(this_is_text: T, *args: Callable[[T], T]) -> T:
    return reduce(lambda arg_1, arg_2: arg_2(arg_1), args, this_is_text)


# Фактори
def factory(class_name: str) -> type:
    return type(class_name, (), {})


# Метакласс для ограничения времени работы методов класса
class LittleMeta(type):

    def __new__(mcs, cls_name: str, superclasses: Tuple[type, ...], attribute_dict: Dict[str, T]) -> type:
        for i in attribute_dict:
            if hasattr(attribute_dict[i], '__call__') and not i.startswith('_'):
                attribute_dict[i] = func_info(attribute_dict[i])
        return type.__new__(mcs, cls_name, superclasses, attribute_dict)


# Класс для проверки метакласса
class Animals(metaclass=LittleMeta):

    def __init__(self, kind: str, name: str, age: [Union[str, int]]) -> None:
        self.kind: str = kind
        self.age: [Union[str, int]] = age
        self.name: str = name

    def age_info(self) -> None:
        time.sleep(1)
        print(f'{self.name} the {self.kind}, he is {self.age} years old!')


if __name__ == '__main__':
    # ВНИМАНИЕ: вывод имени метода при обращении к нему реализован в декораторе!
    # Для флета
    # test = [1, 2, [3, 4, (1, 2, 3, 4), ['i am a string', 7, 8, [9, 10, 11, [12, 13, [14, 15]]]]]]
    # print(list(flat(test)))

    # Для декоратора: первый вариант распечатает текст, второй ничего не сделает
    # time_sleeper(1)
    # time_sleeper(3)

    # Для чейна
    # def shout(text_1: str):
    #     return text_1.upper()
    # exclimination_mark = lambda x: f"{x}!"
    # text = "This is sample string"
    # print(chain_1(text, shout, exclimination_mark))
    # print(chain_2(text, shout, exclimination_mark))

    # Для  фактори
    # for clazz in ["OneClass", "TwoClass", "ThreeClass"]:
    #     print(factory(clazz))

    # Для метакласса
    # animal_1 = Animals('cat', 'Tom', 5)
    # animal_1.age_info()
