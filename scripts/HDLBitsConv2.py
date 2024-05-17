# import json
#
# # Загрузить данные из JSON файла (заменить 'путь/к/файлу.json' на реальный путь)
# with open('data_5_formated.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# new_data = []
# for item in data:
#     # Создать первый вариант записи
#     new_item1 = {
#         'instruction': item['Задание'],
#         'input': item['Текст'],
#         'output': item['Код_1']
#     }
#     new_data.append(new_item1)
#
#     # Создать второй вариант записи
#     new_item2 = {
#         'instruction': item['Задание'],
#         'input': item['Текст'],
#         'output': item['Код_2']
#     }
#     new_data.append(new_item2)
#
# with open('Unslut_HDLB1.json', 'w', encoding='utf-8') as f:
#     json.dump(new_data, f, indent=4, ensure_ascii=False)


import json

# Загрузить данные из JSON файла (заменить 'путь/к/файлу.json' на реальный путь)
with open('datasets_finetune/Unslut_HDLB1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Отфильтровать данные, удаляя записи с пустым "output"
filtered_data = [item for item in data if item['output']]

# Вывести количество записей после фильтрации
print("Количество записей:", len(filtered_data))

# Сохранить отфильтрованные данные в финальный JSON файл (заменить 'путь/к/финальному_файлу.json' на желаемый путь)
with open('datasets_finetune/Unslut_HDLB1_cleared.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)