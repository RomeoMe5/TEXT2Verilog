import json
import re

# Функция для извлечения первого предложения из текста
def get_sentance(text):
    # Используем регулярное выражение для нахождения первого предложения
    # Это упрощенный пример, который ищет точку как конец предложения
    match = re.search(r"([^.]*.)", text)
    if match:
        return match.group(0)
    return ""

# Путь к вашему JSON-файлу
file_path = 'datasets_finetune/data_4.json'

final_path = 'datasets_finetune/data_5_formated.json'

# Загрузка данных из JSON-файла
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Файл не найден.")
    data = []

# Обработка каждой записи в данных
for line in data:
    text = line.get("Текст", "")
    print(text)
    # Вырезаем первое предложение из текста
    sentance = get_sentance(text)
    # Создаем новое поле "Задание" с первым предложением
    print(sentance)
    line["Задание"] = sentance
    line["Текст"] = text.replace(sentance, '', 1)
    # Опционально: удаляем первое предложение из исходного текста
    # запись["текст"] = текст.replace(первое_предложение, '', 1)

# Сохранение обновленных данных обратно в JSON-файл
with open(final_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Обработка завершена.")
