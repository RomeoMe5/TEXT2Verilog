import pandas as pd
import re

# Чтение исходного CSV файла
df = pd.read_csv('datasets_finetune/HDLBitsNorml.csv', names=['text'], header=None)


# Функция для извлечения инструкции, входа и выхода из текста
def extract_data(text):
    instruction_match = re.search(r'Human\s*:\s*(.*?)\s*###', text, re.DOTALL)
    instruction = instruction_match.group(1).strip() if instruction_match else ''

    assistant_part_match = re.search(r'Assistant\s*:(.*?)###', text, re.DOTALL)
    assistant_part = assistant_part_match.group(1).strip() if assistant_part_match else ''

    input_part_match = re.search(r'Assistant\s*:(.*?);', assistant_part, re.DOTALL)
    input_part = input_part_match.group(1).strip() if input_part_match else ''

    output_part = re.sub(r'input\s*.*?;', '', assistant_part).strip()

    if None in [instruction_match, assistant_part_match, input_part_match]:
        return instruction, input_part, output_part, "None present"
    else:
        return instruction, input_part, output_part, "All present"


# Применение функции к каждой строке исходного DataFrame
df['instruction'], df['input'], df['output'], df['status'] = zip(*df['text'].apply(extract_data))

# Запись результата в новый CSV файл
df[['instruction', 'input', 'output', 'status']].to_csv('HDLFormatted_1.csv', index=False)
