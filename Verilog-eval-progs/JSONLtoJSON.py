import json

def convert_jsonl_to_json(jsonl_filepath, json_filepath):
    # Открытие файла JSONL и чтение строк
    data = []
    with open(jsonl_filepath, 'r') as file:
        for line in file:
            try:
                json_object = json.loads(line)
                data.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Запись данных в формат JSON
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Пути к файлам
jsonl_filepath = 'data/VerilogDescription_Human.jsonl'
json_filepath = 'data/VerilogDescription_Human.json'

# Вызов функции
convert_jsonl_to_json(jsonl_filepath, json_filepath)
