import json
from some_llm_library import validate_code

def read_samples(sample_file):
    """Чтение сгенерированных примеров из файла."""
    samples = []
    with open(sample_file, 'r') as file:
        for line in file:
            samples.append(json.loads(line))
    return samples

def write_results(results, output_file):
    """Запись результатов валидации в файл."""
    with open(output_file, 'w') as file:
        for result in results:
            file.write(json.dumps(result) + '\n')

def validate_samples(samples):
    """Валидация списка сгенерированных примеров."""
    results = []
    for sample in samples:
        task_id = sample['task_id']
        completion = sample['completion']
        # Предположим, что validate_code возвращает словарь с результатами валидации
        validation_result = validate_code(task_id, completion)
        results.append({'task_id': task_id, 'validation_result': validation_result})
    return results

def main(sample_file, output_file):
    samples = read_samples(sample_file)
    results = validate_samples(samples)
    write_results(results, output_file)

if __name__ == "__main__":
    sample_file = "path/to/your/samples.jsonl"
    output_file = "path/to/output/validation_results.jsonl"
    main(sample_file, output_file)


