import os
import csv
import subprocess

# Конфигурация
root_dir = "Vgen"  # Путь к папке Vgen с тестбенчами
verilog_dir = "lora3_newData_50step_r128_temp02"  # Путь к папке с Verilog кодами
csv_file_path = "validate_results_llama3_4bit_newData_50step_temp02.csv"  # Путь к файлу CSV с результатами

# Заголовки для файла CSV
headers = ["Subfolder", "Code_Number", "Test_Passed", "Error"]

# Создаем файл CSV и записываем заголовки
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)


# Функция для запуска симуляции и проверки результата
def simulate_and_check(tb_file, v_file):
    # Компилируем Icarus Verilog и сохраняем возможные ошибки
    compile_command = f"iverilog -o out.vvp {tb_file} {v_file}"
    compile_result = subprocess.run(compile_command, shell=True, text=True, capture_output=True)

    if compile_result.returncode != 0:
        # Ошибка компиляции
        return "Fail", compile_result.stderr.strip()

    # Если ошибок нет, выполняем симуляцию
    simulation_command = f"vvp out.vvp"
    simulation_result = subprocess.run(simulation_command, shell=True, text=True, capture_output=True)

    if simulation_result.returncode != 0:
        # Ошибка выполнения
        return "Fail", simulation_result.stderr.strip()

    # Проверяем вывод симуляции на наличие строки, указывающей на успешный тест
    return "Yes" if "all tests passed" in simulation_result.stdout else "No", ""


# Получаем список всех Verilog файлов в папке Vgen_output
verilog_files = [f for f in os.listdir(verilog_dir)]
print(verilog_files)
# Обход всех подпапок в директории тестбенчей
for subdir, dirs, files in os.walk(root_dir):
    subfolder_name = os.path.basename(subdir)
    tb_files = [f for f in files if f.startswith("tb")]

    for tb in tb_files:
        tb_path = os.path.join(subdir, tb)
        for vf in verilog_files:
            if vf.startswith(subfolder_name):
                vf_path = os.path.join(verilog_dir, vf)
                code_number = vf.split('_')[-1].split('.')[0]  # Извлекаем номер из имени файла
                test_result, error_message = simulate_and_check(tb_path, vf_path)
                # Записываем результат в CSV файл
                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([subfolder_name, code_number, test_result, error_message])

# Подсчет метрики Pass@k
with open(csv_file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    results = [row[2] for row in reader]
    pass_count = results.count("Yes")
    total_tests = len(results) - results.count("Fail")
    pass_at_k = pass_count / total_tests if total_tests > 0 else 0
    print(f"Pass@k metric: {pass_at_k:.2f}")
