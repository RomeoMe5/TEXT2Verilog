import json

# Загрузка исходного JSON файла
with open('datasets_finetune/data_5_formated.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразование данных в новый формат
transformed_data = []
for item in data:
    transformed_item = {
        'instruction': item['Задание'],
        'input': item['Текст'],
        'output': item['Код_2']
    }
    transformed_data.append(transformed_item)

# Сохранение преобразованных данных в новый JSON файл
with open('HDLBits_unsl1.json', 'w', encoding='utf-8') as file:
    json.dump(transformed_data, file, ensure_ascii=False, indent=4)

print("Преобразование выполнено и сохранено в 'output.json'.")
