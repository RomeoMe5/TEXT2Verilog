import csv
from collections import defaultdict


# Подсчет метрики Pass@k с группировкой по 'Subfolder'
def calculate_pass_at_k(csv_file_path):
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок

        results_by_subfolder = defaultdict(list)
        for row in reader:
            subfolder = row[0]  # Предполагаем, что столбец 'Subfolder' имеет индекс 1
            result = row[2]  # Предполагаем, что результат находится в третьем столбце
            results_by_subfolder[subfolder].append(result)

        print(results_by_subfolder)
        # Считаем количество групп, где хотя бы один результат - 'Yes'
        pass_count = sum(1 for results in results_by_subfolder.values() if "Yes" in results)
        print(pass_count)
        # Общее количество групп, исключая группы, где все результаты - 'Fail'
        total_groups = sum(1 for results in results_by_subfolder.values() if not all(r == "Fail" for r in results))
        print(total_groups)
        # Расчет Pass@k
        pass_at_k = pass_count / total_groups if total_groups > 0 else 0
        print(f"Pass@k metric: {pass_at_k:.2f}")


# Пример использования
csv_file_path = 'validate_results_llama3_4bit.csv'
calculate_pass_at_k(csv_file_path)
