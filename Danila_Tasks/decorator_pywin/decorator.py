import time
import threading
import math
import os
from multiprocessing import Process
from Danila_Tasks.decorator_pywin.steps import PyWin


times = {}
win = PyWin()


def func_time(func):
    def time_info(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times[args[-1]] = end_time - start_time
    return time_info


@func_time
def multi_thread(*func):
    def info(_):
        if func[-1] == 'multi':
            for x in func[-1]:
                process_multi = Process(target=x())
                process_multi.start()
        if func[-1] == 'thread':
            for x in func[-1]:
                process_thread = threading.Thread(target=x())
                process_thread.start()
    return info


def time_difference():
    multi = times.setdefault('multi')
    thread = times.setdefault('thread')
    if multi > thread:
        print(f'Мультипроцесс работает быстрее на {multi - thread}')
    if thread > multi:
        print(f'Thread работает быстрее на {thread - multi}')


def factor():
    for num in range(100, 200):
        return math.factorial(num)


def writing(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)


def main():
    multi_thread(factor(), writing('text_file', 'heart'), 'multi')
    multi_thread(factor(), writing('text_file', 'stone'), 'thread')
    time_difference()
    win.open_app(r'C:\Program Files (x86)\WinRAR\WinRAR.exe')
    win.set_window('WinRAR')
    win.click('ToolbarДобавить')
    win.set_window()
    win.select_tab_element('TabControl', 'Файлы')
    win.input_path('Добавляемые &файлы:Edit2', os.getcwd() + r'\*.txt')
    win.click('ОК')


if __name__ == '__main__':
    main()
