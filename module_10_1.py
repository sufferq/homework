import time
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open('file_name', 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
        file.close()
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()
time_result = time_stop - time_start
print(f'Время работы функций {time_result}')

time2_start = datetime.now()

thr_first = Thread(target=write_words, args= (10, 'example5.txt'))
thr_second = Thread(target=write_words, args= (30, 'example6.txt'))
thr_third = Thread(target=write_words, args= (200, 'example7.txt'))
thr_fourh = Thread(target=write_words, args= (100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourh.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourh.join()

time2_stop = datetime.now()
time2_result = time2_stop - time2_start
print(f'Время работы потоков {time2_result}')

