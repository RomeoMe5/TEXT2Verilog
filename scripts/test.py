# import pandas as pd
#
# # Загрузка CSV файла
# df = pd.read_csv("train60k.csv")
#
# # Проверка, что в DataFrame есть данные
# if not df.empty:
#     # Получение первой строки DataFrame
#     first_record = df.iloc[0]
#
#     # Вывод каждого атрибута отдельно
#     print("system_prompt:", first_record['system_prompt'])
#     print("instruction:", first_record['instruction'])
#     print("module:", first_record['module'])
#     print("description:", first_record['description'])
#     print("output:", first_record['output'])
#     print("prompt:", first_record['prompt'])
#     print("module_name:", first_record['module_name'])
# else:
#     print("DataFrame пуст.")




# import json
#
# # Функция для чтения данных из JSONL файла
# def read_jsonl(file_path):
#     data = []
#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             data.append(json.loads(line))
#     return data
#
# # Загрузить данные из первого JSONL файла (заменить 'путь/к/файлу1.jsonl' на реальный путь)
# data1 = read_jsonl('verilog-eval/data/VerilogEval_Human.jsonl')
#
# # Загрузить данные из второго JSONL файла (заменить 'путь/к/файлу2.jsonl' на реальный путь)
# data2 = read_jsonl('verilog-eval/descriptions/VerilogDescription_Human.jsonl')
#
# # Создать словарь для быстрого поиска detail_description по task_id
# detail_descriptions = {item['task_id']: item['detail_description'] for item in data2}
#
# # Создать новый список с нужными атрибутами
# new_data = []
# for item in data1:
#     task_id = item['task_id']
#     new_item = {
#         'detail_description': detail_descriptions.get(task_id, ''),  # Получить detail_description по task_id, если он есть
#         'prompt': item['prompt'],
#         'canonical_solution': item['canonical_solution']
#     }
#     new_data.append(new_item)
#
# # Сохранить новый список в JSON файл (заменить 'путь/к/новому_файлу.json' на желаемый путь)
# with open('HDLB161_new_dataset.json', 'w', encoding='utf-8') as f:
#     json.dump(new_data, f, indent=4, ensure_ascii=False)



import json

# Функция для чтения данных из JSONL файла
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# # Загрузить данные из первого JSONL файла (заменить 'путь/к/файлу1.jsonl' на реальный путь)
data1 = read_jsonl('verilog-eval/data/VerilogEval_Human.jsonl')
#
# # Загрузить данные из второго JSONL файла (заменить 'путь/к/файлу2.jsonl' на реальный путь)
data2 = read_jsonl('verilog-eval/descriptions/VerilogDescription_Human.jsonl')

# Создать словарь для быстрого поиска detail_description по task_id
detail_descriptions = {item['task_id']: item['detail_description'] for item in data2}

# Создать новый список с нужными атрибутами и переименовать их
new_data = []
for item in data1:
    task_id = item['task_id']
    new_item = {
        'instruction': detail_descriptions.get(task_id, ''),
        'input': item['prompt'],
        'output': item['canonical_solution']
    }
    new_data.append(new_item)

# Сохранить новый список в JSON файл (заменить 'путь/к/новому_файлу.json' на желаемый путь)
with open('datasets_finetune/HDLB161_new_update.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=4, ensure_ascii=False)

