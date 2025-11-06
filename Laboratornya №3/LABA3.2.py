def format_text(write):
    if write == 'создать новый файл':
        with open(r"C:\Users\kosov\PycharmProjects\PythonProject\user_input.txt", 'w', encoding='utf-8') as file:
            text = input("Введите текст для записи: ")
            file.write(text + '\n')
            return "Файл создан и текст записан."
    elif write == 'дополнить файл':
        with open(r"C:\Users\kosov\PycharmProjects\PythonProject\user_input.txt", 'a', encoding='utf-8') as file:
            text = input("Введите текст для добавления: ")
            file.write(text + '\n')
            return "Текст добавлен в существующий файл."
    else:
        return "Ошибка ввода. Введите 'новый' или 'дополнить'."


print("Вы хотите создать новый файл или дополнить существующий?")
print(format_text(input().strip()))
