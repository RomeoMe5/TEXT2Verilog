import json

# Пути к JSON файлам, которые нужно объединить
file_path1 = 'HDLBits_unsl1.json'
file_path2 = 'datasets_finetune/train60k_uslat.json'

# Чтение первого файла
with open(file_path1, 'r', encoding='utf-8') as file:
    data1 = json.load(file)

# Чтение второго файла
with open(file_path2, 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# Объединение данных
combined_data = data1 + data2

# Сохранение объединённых данных в новый JSON файл
with open('datasets_finetune/train61k_uslt.json', 'w', encoding='utf-8') as file:
    json.dump(combined_data, file, ensure_ascii=False, indent=4)

print("Данные из двух файлов успешно объединены в 'combined_file.json'.")
