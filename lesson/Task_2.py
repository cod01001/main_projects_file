import csv
import json
import time


# 1. Напишите программу на Python, которая принимает на вход строку и проверяет, состоит ли она только из цифр.
# Если да, программа должна вывести сумму всех цифр, если нет - вывести сообщение о том, что строка не является числом.
def is_int_or_not(x):
    if x.isdigit():
        y = 0
        for i in str(x):
            y += int(i)
        print(y)
    else:
        print('строка не является числом')


# t = is_int_or_not('3111')


# 2. Создайте программу на Python, которая считывает данные из текстового файла и выводит количество слов в файле,
# количество символов и самые часто встречающиеся слова.


def read():
    csv_csv_file = open('read.txt', encoding='UTF-8')
    student_csv_file_writer_open = csv.reader(csv_csv_file, delimiter=';')

    for i in student_csv_file_writer_open:
        quantity_symbols = 0
        word = []
        word_quantity = 0
        for i2 in i:
            count = len(i2.split())
            print('количество слов', count)
            for i3 in i2.split():
                quantity_symbols += len(i3)
                o = i2.split().count(i3)
                if o > word_quantity:
                    word_quantity = i2.split().count(i3)
                    word.clear()
                    word.append(i3)
        print('количество символов', quantity_symbols)
        print('слово', word, 'повторяется', word_quantity, 'раз')




# 3. Создайте декоратор на Python, который выводит время выполнения функции.
def track_of_time_decorator(func):
    def track_of_time():
        start = time.time()
        func()
        finish = time.time()
        print(f'Время выполнения функции "{func.__name__}": {(finish - start)} секунд')

    return track_of_time()
#track_of_time_decorator(read)



# 4. Создай программу, которая будет читать json файл с данными о продуктах (название, цена, количество)
# и выводить информацию о продукте с самой высокой ценой.

# открытие файла в формате чтения и юникода UTF-8
# with open('products.json','r',encoding='utf-8') as file:
#     data = json.load(file)
#     x = 0
#     x2 = ''
#     for i,i2 in data.items():
#         if i2[1] > x:
#             x2 = i
#             x = i2[1]
#         else:
#             continue

#print(x2)



# 5. Напиши скрипт, который будет считывать данные из csv файла с информацией о студентах (имя, возраст, средний балл)
# и создавать новый csv файл, в котором будут только студенты с возрастом от 18 до 25 лет и средним баллом выше 4.
# with open('student_csv_file.csv',encoding='utf-8') as file:
#     data = csv.reader(file)
#     for i in data:
#         if int(i[1]) > 21 and float(i[3]) > 4:
#             print(i)
#             with open('new_student_csv_file.csv','a',encoding='utf-8') as reda_new:
#                 writer = csv.writer(reda_new)
#                 writer.writerow(i)



# 6. Разработай программу, которая будет обрабатывать исключения при чтении файла и
# выводить пользователю сообщение о возникшей ошибке.

# 7. Напиши скрипт, который будет принимать на вход список слов и создавать словарь, в котором ключами будут
# первые буквы слов, а значениями - списки слов, начинающихся с этой буквы.

# def dict_word(sp):
#     word_count = set()
#     dict_word = {}
#     for i in sp:
#         word_count.add(i[0])
#
#     for i2 in sp:
#         t = []
#         for i3 in word_count:
#             if i3 == i2[0]:
#                 print(i2)
#                 t.append(i2)
#                 dict_word[i3] = t
#     print(dict_word)




# решить потом на свежую голову
# сейчас не могу осилить
# нет слов, одни буквы
def dict_word(sp):
    word_count = set()
    dict_word = {}
    x = []
    for i in sp:
        word_count.add(i[0])


    for i2 in sp:
        if i2 in word_count:
            x.append(i2)

    print(word_count)

    #print(word_count)
sp = ["apple", "banana", "orange", "grape", "kiwi", "pear", "peach", "plum", "cherry"]
dict_word(sp)

#{'a', 'k', 'g', 'b', 'c', 'o', 'p'}





