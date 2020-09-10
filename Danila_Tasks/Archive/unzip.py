import os.path
import rarfile
import shutil


def folder():
    """Функция проверяет, существует ли каталог
    на диске С, если да, то удаляет его со всем
    содержимым.
    """
    check_file = os.path.exists('C:\\1')
    if check_file:
        shutil.rmtree('C:\\1', ignore_errors=False, onerror=None)


def unzip():
    """Функция распаковывает архив на диск С.
    Если каталог не существует, то создаёт его.
    """
    fantasy_zip = rarfile.RarFile('C:\\Users\\de\\PyCharmProjects\\'
                                  'Exception\\venv\\Archive\\1.rar')
    fantasy_zip.extractall('C:\\1')


def files_in_zip():
    """Функция ищет файлы и папки в каталоге.
    Выводит список папок и файлов
    и печатает их кол-во.
    """
    dirs_list = []
    files_list = []
    for root, dirs, files in os.walk('C:\\1'):
        for f in files:
            files_list.append(f.split('.')[0])
    for r, d, f in os.walk('C:\\1'):
        for dirs in d:
            dirs_list.append(dirs)
    print(dirs_list + files_list)
    print(f'Папок в каталоге: {len(dirs_list)} \n'
          f'Файлов в каталоге: {len(files_list)}')


if __name__ == '__main__':
    folder()
    unzip()
    files_in_zip()
