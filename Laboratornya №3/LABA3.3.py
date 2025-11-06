def format_text(write):
    try:
        if write == 'целиком':
            with open(r"C:\Users\kosov\PycharmProjects\PythonProject\example.txt", 'r', encoding='utf-8') as file:
                return file.read()
        elif write == 'построчно':
            with open(r"C:\Users\kosov\PycharmProjects\PythonProject\example.txt", 'r', encoding='utf-8') as file:
                return file.readlines()
        else:
            return 'Ошибка ввода'
    except FileNotFoundError:
        return 'Файл не найден. Проверьте путь или имя файла.'

print('Какой формат чтения вы хотите выбрать?')
print('чтение целиком или построчно?')
print(*format_text(input().strip()), sep='')
