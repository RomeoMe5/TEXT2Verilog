# import pandas as pd
#
# # Загрузка данных
# df = pd.read_csv('random_20000_records_1.csv')
#
# # Проверка на достаточное количество строк
# if len(df) < 800:
#     raise ValueError("Файл содержит менее 800 записей.")
#
# # Случайный выбор 800 записей
# selected_data = df.sample(n=500, random_state=923)  # Устанавливаем random_state для воспроизводимости
#
# # Сохранение в новый CSV файл
# selected_data.to_csv('selected_500_records.csv', index=False)
#
#
import pandas as pd
file_path1 = 'datasets_finetune/combined_data_1.csv'

data1 = pd.read_csv(file_path1)

print(data1.info())
print(data1.tail())

#
# # Пути к файлам CSV
# file_path1 = 'selected_500_records.csv'
# file_path2 = 'HDLBitsNorml.csv'
#
# # Загрузка данных из каждого файла
# data1 = pd.read_csv(file_path1)
# data2 = pd.read_csv(file_path2)
#
# # Объединение файлов
# combined_data = pd.concat([data1, data2], ignore_index=True)
#
# # Сохранение объединенных данных в новый файл CSV
# combined_data.to_csv('combined_data_1.csv', index=False)

