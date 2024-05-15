import os

# Задайте директорию с файлами
directory = './'

# Задайте текст, который нужно удалить
text_to_remove = ""

# Проходим по всем файлам в указанной директории
for filename in os.listdir(directory):
    # Полный путь к файлу
    file_path = os.path.join(directory, filename)

    # Проверяем, что это файл, а не директория
    if os.path.isfile(file_path):
        # Читаем содержимое файла
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Удаляем указанный текст из содержимого файла
        content = content.replace(text_to_remove, "")

        # Перезаписываем файл с новым содержимым
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)