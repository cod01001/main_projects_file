import csv

# открытие файла в формате чтения и юникода UTF-8
student_csv_file = open('../lesson/student_csv_file.csv', encoding='UTF-8')
# говорим что будет считывать из csv файла
student_csv_file_writer_open = csv.reader(student_csv_file, delimiter=';')

for i in student_csv_file_writer_open:
    print(i)

#print(student_csv_file_writer_open)
