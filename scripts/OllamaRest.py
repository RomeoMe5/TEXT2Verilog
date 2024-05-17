import requests
import json
from datetime import datetime
import argparse
import csv
from fuzzywuzzy import fuzz
import os

def custom_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}"
    with open('ollama_api_custom.log', 'a', encoding='utf-8') as log_file:
        log_file.write(log_message + '\n')


class OllamaAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        custom_log(f"API initialized with base URL: {base_url}")

    def list_model(self):
        custom_log("Listing all models")
        response = requests.get(f"{self.base_url}/tags")
        return response.json()

    def info_model(self, name):
        custom_log(f"Fetching information for model: {name}")
        data = {
            "name": name
        }
        response = requests.post(f"{self.base_url}/show", json=data)
        return response.json()

    def generate_model(self, name, prompt):
        custom_log(f"Generating model output for: {name} with prompt")
        data = {
            "model": name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "seed": 123,
                "temperature": 0
            }
        }
        response = requests.post(f"{self.base_url}/generate", json=data)
        # print(response)
        # print(json.loads(response.text)['response'])
        return json.loads(response.text)


def analBib(biblist):
    content = ''
    with open(biblist, 'r', encoding='utf-8') as file:
        num = 1
        for line in file:
            content += str(num) + '.' + line
            num += 1

    return content


def find_page_number(csv_file_path, substring, threshold=70):
    results = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2:
                continue  # Skip rows that don't have enough columns
            page_number, page_text = row
            match_percentage = fuzz.partial_ratio(page_text, substring)
            if match_percentage >= threshold:
                results.append((int(page_number), match_percentage))

    return results


def main():
    parser = argparse.ArgumentParser(description="Run Ollama API client with custom settings.")
    parser.add_argument("--port", type=str, help="The port number where the API is running.")
    parser.add_argument("--model", type=str, help="The name of the model to use.")
    parser.add_argument("--biblist", type=str, help="File path for the bibliography list.")
    parser.add_argument("--content", type=str, help="File path for the content file.")
    parser.add_argument("--page", type=str, help="File path to csv with pages.")
    parser.add_argument("--output", type=str, help="File path to csv results.")

    args = parser.parse_args()

    base_url = f"http://localhost:{args.port}/api"
    api = OllamaAPI(base_url)
    bibliography = analBib(args.biblist)
    with open(args.content, 'r', encoding='utf-8') as file:
        content = file.read()
    print(bibliography)

    cont_list = bibliography.split('\n')
    page_list = []
    for cont in cont_list:
        matching_pages = find_page_number(args.page, cont)
        if matching_pages:
            print(matching_pages[0][0])
            page_list.append(matching_pages[0][0])

    print('_______')

    prompt = content + '\n' + bibliography + '\n' + 'В ответе к каждой записи написать один из двух вариантов: Да, НЕТ.'
    # print(prompt)
    output = api.generate_model(args.model, prompt)
    i = 0
    with open(args.output, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Page', 'Text', 'Error'])  # Writing header
        for bibl in output['response'].split('\n'):
            print(page_list[i], cont_list[i], bibl)
            writer.writerow([page_list[i], cont_list[i], bibl])
            i = i + 1

if __name__ == "__main__":
    #main()
    api = OllamaAPI("http://localhost:11434/api")
    # print(api.list_model())
    # #print(api.info_model('llama2'))
    # with open('test.txt', 'r', encoding='utf-8') as file:
    #     content = file.read()
    #
    # prompt = content + '\n' + analBib('VRK_Korchagin_DATASET_RISCV_v2R.pdf_lterature.txt') + '\n' + 'В Ответе к каждой записи написать один из вдух вариантов: Да, НЕТ.'
    # print(prompt)

    # Задаем корневую директорию
    root_dir = 'Vgen'
    content = ''

    # Проходим по всем директориям и файлам в корневой директории
    for subdir, dirs, files in os.walk(root_dir):
        num = 0
        for file in files:
            # Проверяем, содержит ли имя файла 'prompt'
            if 'prompt' in file:
                # Формируем полный путь к файлу
                print(file)
                print(subdir)
                file_path = os.path.join(subdir, file)
                num = num + 1
                # Читаем содержимое файла и добавляем его в переменную content
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(content)
                    print('____')
                    output = api.generate_model('llama3:8b', content)
                    print(output['response'])
                    with open('Vgen_output'+'\\'+subdir[5:]+'_'+str(num), 'w') as output_file:
                        output_file.write(output['response'])



    # Выводим содержимое считанных файлов
    print(content)


    # print(analBib())

    # print(output['response'])



