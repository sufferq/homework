import os
import time

def path_info(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.walk(root)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
                    f' Время изменения: {formatted_time}, Родительская директория:'
                    f' {parent_dir}')

if __name__ == '__main__':
    path_info('.')