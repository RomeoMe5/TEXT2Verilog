import pandas as pd
import random

# Заменить 'путь/к/файлу.csv' на настоящий путь к вашему CSV файлу
data = pd.read_csv('datasets_finetune/train.csv')

# Получить количество строк в DataFrame
num_rows = len(data)

# Выбрать случайное количество строк (например, 5)
num_random_rows = 5

# Выбрать случайные индексы строк
random_indices = random.sample(range(num_rows), num_random_rows)

# Отобразить случайные строки
random_rows = data.iloc[random_indices]
print(random_rows)