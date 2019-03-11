# easy
# Задача№1
import os
print('dir_1 - dir_9 {}'.format(os.getcwd()))
def makedir(i):
    os.mkdir('{}'. format(i))
def removed(i):
    os.rmdir('{]'.format(i))
# Задача №2
import os
def nowdir():
    print('Содержимое текущй папки: {}'.format(os.listdir()))

# Задача№3
import shutil
shutil.copy('test4.py')

 # normal
 # Задача№
if __name__ == '__main__':
    print('---------------------Задача №1 (normal)----------------------')

import os
import Less5

def change_dir (path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))

def start ():
    answer =''
    while answer != '5':
        print('----------------------------------------')
        print('Текущая директория: ' + os.getcwd())
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer =='5':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(change_dir(path_name))
        elif answer == '2':
            Less5.list_dir()
        elif answer == '3':
            name = input('Введите имя удаляемой папки: ')
            Less5.remove_dir(name)
        elif answer == '4':
            name = input('Введите имя новой папки: ')
            Less5.make_dir(name)

if __name__ == '__main__':
    start()