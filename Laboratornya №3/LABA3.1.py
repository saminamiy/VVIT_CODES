def format_text(write):
    if write == 'целиком':
        with open(r"C:\Users\kosov\PycharmProjects\PythonProject\example.txt", 'r', encoding='utf-8') as file:
            return file.read()
    elif write == 'построчно':
        with open(r"C:\Users\kosov\PycharmProjects\PythonProject\example.txt", 'r', encoding='utf-8') as file:
            return file.readlines()
    else:
        return 'Ошибка ввода'
print('Какой формат чтения вы хотите выбрать?','\n' + 'чтение целиком или построчно?')
print(*format_text(input()), sep='')