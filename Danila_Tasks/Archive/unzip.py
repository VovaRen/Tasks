import os.path
import rarfile
import shutil
path_arch = 'C:\\1'


def folder():
    check_file = os.path.exists(path_arch)
    if check_file:
        shutil.rmtree(path_arch, ignore_errors=False, onerror=None)


def unzip():
    fantasy_zip = rarfile.RarFile('C:\\Users\\de\\PyCharmProjects\\'
                                  'Exception\\venv\\Archive\\1.rar')
    fantasy_zip.extractall(path_arch)


def files_in_zip():
    dirs_list = []
    files_list = []
    for root, dirs, files in os.walk(path_arch):
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
