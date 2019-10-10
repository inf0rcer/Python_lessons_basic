# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys
import shutil

dir_name = [('dir_' + str(i + 1)) for i in range(9)]

def make_dir(path):
    dir_loc = os.path.join(os.getcwd(), path)
    try:
        os.mkdir(dir_loc)
        print(' -- папка успешно создана')
    except:
        print(dir_loc + ' -- папка уже существует')


for i in dir_name:
    make_dir(i)

def remove_dir(path):
    dir_loc = os.path.join(os.getcwd(), path)
    try:
        os.rmdir(dir_loc)
        print(' -- папка успешно удалена')
    except:
        print(dir_loc + ' -- такой папки не существует')
    pass

for i in dir_name:
    remove_dir(i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
path = os.getcwd()
def view_directories(path):
    for _ in os.listdir(path):
        print(_)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#def copy_file(orig_file, clone_file):
#    shutil.copy(orig_file, clone_file)


#orig_file = sys.argv[0]
#clone_file = orig_file + '.copy'
#copy_file(orig_file,clone_file)


#ДЛЯ ИМПОРТА В NORMAL
def change_dir(path):
    try:
        os.chdir(path)
        print(os.getcwd() + ' -- текущая директория')
    except:
        print(dir_path + ' -- такой директории не существует')