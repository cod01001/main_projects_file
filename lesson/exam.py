import csv

# начало 8:12
# Задание №1
#
# У вас есть задача создать систему учета студентов в университете.
#
# 1. Определите структуру данных для хранения информации о студентах, включая их имя, возраст, курс, средний балл и список сданных экзаменов.
# Выброна структура данных CSV

print('Здравствуй пользователь, тебя приветствует система учета студентов колледжа имени Яны Сергеевны Щавель\n')


def add_new_student(student_name, student_age, student_course, students_GPA = 'Средний балл студента: ',
                    list_of_passed_exams = 'Количество сданных экзаменов: ',
                    theory_exam_1 = 'Экзамен по практике: экзамена еще не было, '
                                  'Экзамен по теории: экзамена еще не было,'
                                  'Экзамен заключительный: экзамена еще не было,',
                    final_grades ='Оценка по практике: экзамена еще не было, '
                                  'Оценка по теории: экзамена еще не было,'
                                  'Оценка заключительный: экзамена еще не было,'
                    ):

    # открытие файла в формате записи и юникода UTF-8
    student_csv_file = open('student_csv_file.csv', 'a', encoding='UTF-8', newline='')

    # говорим что будет записывать в csv файл и как будет записывать
    student_csv_file_writer_open = csv.writer(student_csv_file,delimiter=';')

    # вводим информацию которую хотим добавтиь и в каком порядке будут записыватья файлы
    student_csv_file_writer = [f"{student_name};{student_age};{student_course};{students_GPA};"
                               f"{list_of_passed_exams};{theory_exam_1};{final_grades}"]

    # момент внеселия информации в файл
    student_csv_file_writer_open.writerow(student_csv_file_writer)

    # закрытие файла
    student_csv_file.close()

def main():
    user_enters_commands = input(f'''Введите запрос
Добавить нового студента в базу данных колледжа - 1.
Провести экзамен у студентов - 2\n''')


    if user_enters_commands == '1':
        name_student_dcc = input('Введите имя студента: ')
        age_student_dcc  = input('Введите возраст студента: ')
        course_student_dcc  = input(f'''Доступны вакансии: 
Backend Developer - 1,
Frontend developer - 2
Network Manager - 3
Введите курс студента: ''')


# добавление нового ученика -------------------------------------------------
        if course_student_dcc == '1':
            course_student_dcc = 'Backend Developer'
            student_obgect = add_new_student(name_student_dcc, age_student_dcc, course_student_dcc)
            print(f'Студент: {name_student_dcc}, '
                  f'возраст: {age_student_dcc}, курс: {course_student_dcc} добавлен в систему')

        elif course_student_dcc == '2':
            course_student_dcc = 'Frontend developer'
            student_obgect = add_new_student(name_student_dcc, age_student_dcc, course_student_dcc)
            print(f'Студент: {name_student_dcc}, '
                  f'возраст: {age_student_dcc}, курс: {course_student_dcc} добавлен в систему')

        elif course_student_dcc == '3':
            course_student_dcc = 'Network Manager'
            student_obgect = add_new_student(name_student_dcc, age_student_dcc, course_student_dcc)
            print(f'Студент: {name_student_dcc}, '
                  f'возраст: {age_student_dcc}, курс: {course_student_dcc} добавлен в систему')

        elif course_student_dcc != ['1','2','3']:
            print('Введите корректно название курса \n')
            main()
# ---------------------------------------------------------------------------




# проведение экзамена ---------------------------------------------------------------------------

    elif user_enters_commands == '2':
        user_enters_commands_exam = input('Хотите провести экзамен у курса или у отдельно выбраных учеников?\n'
                              'Если у курсу выберите - 1\n'
                              'Если у отдкльных учеников выберите - 2\n')


        if user_enters_commands_exam == '1':
            user_enters_commands_exam_chainch = input('По какому курсу вы хотите провести экзамен?\n'
                                                    'Backend Developer - 1\n'
                                                    'Frontend developer - 2\n'
                                                    'Network Manager - 3\n')
            if user_enters_commands_exam_chainch == '1':
                user_enters_commands_exam_chainch_exam_name = input('По какому экзамену вы хотите провести тест?\n'
                                                          'Экзамен по практике - 1\n'
                                                          'Экзамен по теории - 2\n'
                                                          'Эаключительный экзамен- 3\n')
                if user_enters_commands_exam_chainch_exam_name == '1':
                    # открытие файла в формате чтения и юникода UTF-8
                    student_csv_file = open('student_csv_file.csv', encoding='UTF-8')

                    # говорим что будет считывать из csv файла
                    student_csv_file_writer_open = csv.reader(student_csv_file, delimiter=';')

                    print('Студенты участвующие в экзамене по практике курса Backend Developer: ')
                    for i in student_csv_file_writer_open:
                        if i[2] == 'Backend Developer':
                            print(i[0])


#---------------------------------------------------------------------------
main()

# 2. Напишите методы для автоматического определения академической стипендии на основании среднего балла студента и его успеваемости.
#
# 3. Реализуйте метод для расчета общего среднего балла по списку студентов.
#
# 4. Создайте функции для сохранения информации о студентах в файле, а также для загрузки этой информации из файла.
#
# 5. Напишите методы для расчета возможности перевода студента на следующий курс, а также для добавления и удаления экзаменов у студента.
#
# 6. Разработайте классы для представления студентов и университета, а также методы для взаимодействия с этими объектами.
#
# 7. Примените декораторы для реализации логирования операций по учету студентов.















