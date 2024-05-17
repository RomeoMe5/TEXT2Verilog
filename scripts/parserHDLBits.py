from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = Options()
options.headless = True  # Или False, если хотите видеть процесс в браузере
driver = webdriver.Firefox(options=options)

# Начальный URL сайта
url = "https://hdlbits.01xz.net/wiki/Step_one"

data = []


while True:
    try:
        driver.get(url)
        # Ожидание для загрузки страницы
        driver.implicitly_wait(10)
        # Выводим заголовок страницы
        naming = '_'.join(driver.title[:-10].lower().split())
        print(naming)

        # Находим элемент, в котором рендерится CodeMirror
        code_mirror_element = driver.find_element(By.CSS_SELECTOR, "div.CodeMirror")
        # Очищаем содержимое CodeMirror с помощью JavaScript
        driver.execute_script("arguments[0].CodeMirror.setValue('');", code_mirror_element)

        # Указываем путь к файлу
        file_path = 'hdlbits-solutions/solutions/'+naming+'.v'
        print(file_path)
        try:
            # Открываем файл для чтения
            with open(file_path, 'r', encoding='utf-8') as file:
                # Читаем все строки файла и объединяем их в одну строку
                all_text = ''.join(file.readlines())

        except:
            print("Левый файл для {}".format(naming))




        # Получаем и выводим текст всех тегов <p> на странице
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        full_text = ''
        for paragraph in paragraphs:
            full_text = full_text+paragraph.text

        links = driver.find_elements(By.CSS_SELECTOR, "a.vlgstat_link")

        # Найти элемент <textarea> внутри CodeMirror и ввести текст
        # Возможно, вам нужно будет адаптировать селектор, чтобы точно нацелиться на нужный элемент
        code_mirror_textarea = driver.find_element(By.CSS_SELECTOR, "div.CodeMirror > div > textarea")
        code_mirror_textarea.send_keys(all_text)

        # Если прямая вставка в textarea не срабатывает, попробуйте использовать скрипт для вставки текста
        # driver.execute_script("arguments[0].CodeMirror.setValue('Ваш текст для вставки');", code_mirror_textarea)
        # Найти кнопку по её идентификатору и выполнить нажатие
        driver.implicitly_wait(100)
        submit_button = driver.find_element(By.ID, "submitiframe")
        driver.implicitly_wait(100)
        submit_button.click()
        time.sleep(30)

        ###
        try:
            # Поиск div с id="solnbox"
            solnbox = driver.find_element(By.ID, "solnbox")
            # Получение значения CSS свойства display для этого элемента
            display_style = solnbox.value_of_css_property("display")

            if display_style == "none":
                print("Родительский элемент скрыт (display: none).")
                # Если время ожидания истекло, и элемент так и не был найден, выполняем альтернативные действия
                print("Элемент не найден, выполняем альтернативные действия.")
                # Здесь могут быть любые другие действия, например, переход на другую страницу или закрытие браузера
                line = {
                    'Заголовок': driver.title[:-10],
                    'Текст': full_text,
                    'Код_1': all_text,
                    'Код_2': ''
                }
            else:
                try:
                    sol_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "solnbox_show"))
                    )
                    print("Родительский элемент видим (display: не none).")
                    time.sleep(5)
                    print("Элемент найден, выполняем действия.")
                    sol_button.click()

                    time.sleep(1)
                    print('Получение решения')
                    # Используйте JavaScript для получения текста из второго объекта CodeMirror
                    text_from_second_codemirror = driver.execute_script(
                        "return document.querySelectorAll('.CodeMirror')[1].CodeMirror.getValue();"
                    )

                    print(text_from_second_codemirror)

                    line = {
                        'Заголовок': driver.title[:-10],
                        'Текст': full_text,
                        'Код_1': all_text,
                        'Код_2': text_from_second_codemirror
                    }
                except:
                    print('qqqqqqqqqq')

        except NoSuchElementException:
            print("нету его")
        ###

        print('Нажатие на кнопку')
        try:
            # Пытаемся найти элемент в течение 10 секунд
            sol_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "solnbox_show"))
            )
            print(sol_button)
            time.sleep(5)
            # Если элемент найден, выполняем необходимые действия с ним
            print("Элемент найден, выполняем действия.")
            sol_button.click()

            time.sleep(1)
            print('Получение решения')
            # Используйте JavaScript для получения текста из второго объекта CodeMirror
            text_from_second_codemirror = driver.execute_script(
                "return document.querySelectorAll('.CodeMirror')[1].CodeMirror.getValue();"
            )

            print(text_from_second_codemirror)

            line = {
                'Заголовок': driver.title[:-10],
                'Текст': full_text,
                'Код_1': all_text,
                'Код_2': text_from_second_codemirror
            }

        except TimeoutException:
            # Если время ожидания истекло, и элемент так и не был найден, выполняем альтернативные действия
            print("Элемент не найден, выполняем альтернативные действия.")
            # Здесь могут быть любые другие действия, например, переход на другую страницу или закрытие браузера
            line = {
                'Заголовок': driver.title[:-10],
                'Текст': full_text,
                'Код_1': all_text,
                'Код_2': ''
            }

        data.append(line)


        if len(data) == 97:
            break

        with open('datasets_finetune/data_4.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


        if len(links) > 1:
            second_link = links[1]
            url = second_link.get_attribute('href')
            # print(f"Переход по второй ссылке: {url}")
        else:
            print("Вторая ссылка не найдена. Завершение работы.")
            break
        # print(f"Переход по ссылке: {url}")

    except NoSuchElementException:
        # Если ссылка не найдена, выходим из цикла
        print("Ссылка для перехода не найдена. Завершение работы.")
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        break


with open('datasets_finetune/data_4.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Закрываем драйвер после завершения работы
driver.quit()
