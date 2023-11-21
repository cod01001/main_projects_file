import csv

#print('Здравствуй пользователь, тебя приветствует система учета студентов колледжа имени Яны Сергеевны Щавель\n')

class Student:
    def __init__(self,student_name, student_age, student_course):
        self.student_name = student_name
        self.student_age = student_age
        self.student_course = student_course
        self.list_of_passed_exams = []
        self.gpa_student = 0
    def add_passed_exames(self,grade):
        self.list_of_passed_exams.append(grade)
        self.gpa_student = sum(self.list_of_passed_exams) / len(self.list_of_passed_exams)
        return self.gpa_student



    # 5. Напишите методы для расчета возможности перевода студента на следующий курс,
    # а также для добавления и удаления экзаменов у студента.
    def transferring_a_student_to_the_next_course(self):
        if len(self.list_of_passed_exams) > 5 and self.gpa_student > 3:
            self.student_course += 1
            return self.student_name,' перешел на ',self.student_course,' курс.'
        elif len(self.list_of_passed_exams) < 5 or self.gpa_student < 3:
            return 'студент пока не может перейти на следующий курс'



    def scholarship(self):
        return 'У студента: ' + self.student_name + ' степендия ' + str((self.gpa_student * 0.2) * 2000)

    def del_examen(self):
        self.list_of_passed_exams.pop()
    def course_information(self):
        return 'ученик '+self.student_name+' на ' +  str(self.student_course) + ' курсе'
    def GPA_for_return(self):
        return 'У ученика: ' + self.student_name + ' средний балл ' + str(self.gpa_student)

    # 3. Реализуйте метод для расчета общего среднего балла по списку студентов.
    @staticmethod
    def overall_gpa():
        with open('student_csv_file.csv', 'r', encoding='UTF-8', newline='') as f:
            writer = csv.reader(f)
            x = 0
            p = 0
            for i in writer:
                p += 1
                print(i)
                x += float(i[3])

        print('Средний балл всех студентов',x / p)



class University:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def dell_student(self,student):
        self.students.remove(student)

    def total_gpa_students(self):
        total_gpa_students = [i.gpa_student for i in self.students]
        return sum(total_gpa_students) / len(self.students)

    def student_save_file(self):
        # открытие файла в формате записи и юникода UTF-8
        with open('student_csv_file.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            #writer.writerow(['Имя','возраст','курс','средний балл'])
            for student in self.students:
                writer.writerow([student.student_name,student.student_age,student.student_course,student.gpa_student])


student_1 = Student('Mark', '22', 1)
student_2 = Student('Kiril', '24', 1)
student_3 = Student('Masha', '25', 1)

student_1.add_passed_exames(4)
student_1.add_passed_exames(5)
student_1.add_passed_exames(3)


student_2.add_passed_exames(2)
student_2.add_passed_exames(4)
student_2.add_passed_exames(3)

student_3.add_passed_exames(5)
student_3.add_passed_exames(5)
student_3.add_passed_exames(5)


mgsiit = University()
mgsiit.add_student(student_1)
mgsiit.add_student(student_2)
mgsiit.add_student(student_3)

mgsiit.student_save_file()

l = student_1.transferring_a_student_to_the_next_course()
print(l)
# средний балл всех студентов
# Student.overall_gpa()




# 4. Создайте функции для сохранения информации о студентах в файле, а также для загрузки этой информации из файла.

# 7. Примените декораторы для реализации логирования операций по учету студентов.

