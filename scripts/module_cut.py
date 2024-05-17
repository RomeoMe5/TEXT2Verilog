import os


def process_files(directory):
    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(directory):
        # Полный путь к файлу
        file_path = os.path.join(directory, filename)

        # Убедимся, что это файл, а не директория
        if os.path.isfile(file_path):
            # Читаем содержимое файла и удаляем строки с комментариями
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Фильтруем строки, удаляя те, что начинаются с //
            filtered_lines = [line for line in lines if not line.strip().startswith('//')]

            # Преобразуем список отфильтрованных строк обратно в строку
            content = ''.join(filtered_lines)

            # Находим начало и конец интересующего нас блока
            start_index = content.find('module')
            end_index = content.find('endmodule')

            # Если найдены оба индекса, обрезаем содержимое и переписываем файл
            if start_index != -1 and end_index != -1:
                # Включаем 'endmodule' в результат
                new_content = content[start_index:end_index + len('endmodule')]
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)


# Задайте путь к директории с файлами
directory_path = 'llama2-13b-FT'
process_files(directory_path)
