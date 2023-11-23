import logging

def log_operation(x, y, result):
    try:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Операция: {x} + {y} = {result}\n')
    except Exception as e:
        print(f'Произошла ошибка при записи в файл: {e}')

def my_function(x, y):
    try:
        result = x + y
        log_operation(x, y, result)
        return result
    except Exception as e:
        print(f'Произошла ошибка при выполнении операции: {e}')

result = my_function(2, 3)
print(f'Результат: {result}')
