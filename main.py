import pandas as pd
import json

# Загрузка данных из CSV файла
df = pd.read_csv("datasets_finetune/train60k.csv")

# Обработка данных
transformed_data = []
for _, row in df.iterrows():
    # Конкатенация system_prompt и instruction
    instruction = f"{row['system_prompt']} {row['instruction']}".strip()

    # Извлечение текста из output до первого знака ";"
    input_text = row['output'].split(';', 1)[0].strip() if ';' in row['output'] else row['output'].strip()

    # Создание словаря для каждой записи
    record = {
        'instruction': instruction,
        'input': input_text+';',
        'output': row['output']
    }
    transformed_data.append(record)

# Сохранение данных в JSON файл
with open('datasets_finetune/train60k_uslat.json', 'w', encoding='utf-8') as file:
    json.dump(transformed_data, file, ensure_ascii=False, indent=4)

print("Преобразование выполнено и сохранено в 'output.json'.")
