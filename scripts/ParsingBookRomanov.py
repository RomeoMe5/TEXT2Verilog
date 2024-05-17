# import fitz  # PyMuPDF
# import re
# from pprint import pprint
#
#
#
# def read_pdf_file(file_path):
#     doc = fitz.open(file_path)
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     doc.close()
#     return text
#
#
# text = read_pdf_file('Цифровой_синтез_Практический_курс.pdf')
#
# # Паттерны для поиска
# listing_pattern = re.compile(r"Листинг\s+\d+\.\d+\s+.*")
# verilog_pattern = re.compile(r"(module[\s\S]*?endmodule)")
#
# # Находим все описания листингов
# listings = listing_pattern.findall(text)
#
# results = []
#
# for listing in listings:
#     start_pos = text.find(listing)
#     preceding_text = text[:start_pos]
#     verilog_matches = verilog_pattern.findall(preceding_text)
#     if verilog_matches:
#         closest_verilog_code = verilog_matches[-1]
#         results.append((closest_verilog_code, listing))
#
# # Определите имя файла для сохранения результатов
# output_file = 'output_Цифровой_синтез.txt'
#
# with open(output_file, 'w', encoding='utf-8') as file:
#     for verilog_code, listing_description in results:
#         file.write("Блок кода Verilog:\n")
#         file.write(verilog_code)
#         file.write("\nОписание листинга:\n")
#         file.write(listing_description)
#         file.write("\n-----\n\n")


import fitz  # PyMuPDF
import re
from pprint import pprint


def read_pdf_file(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


text = read_pdf_file('Цифровой_синтез_Практический_курс.pdf')

# Паттерны для поиска листингов или примеров
listing_pattern = re.compile(r"(Листинг|Example|example|listing|Listing)\s+\d+\.\d+\s+.*")
verilog_pattern = re.compile(r"(module[\s\S]*?endmodule)")

# Находим все описания листингов или примеров
listings = listing_pattern.findall(text)

results = []

# Ищем код Verilog до или после найденного листинга или примера
for listing in listings:
    pos = text.find(listing)
    # Поиск кода до листинга
    preceding_text = text[:pos]
    following_text = text[pos + len(listing):]

    preceding_matches = verilog_pattern.findall(preceding_text)
    following_matches = verilog_pattern.findall(following_text)

    if preceding_matches:
        closest_preceding_verilog = preceding_matches[-1]
        results.append((closest_preceding_verilog, listing, "before"))
    if following_matches:
        closest_following_verilog = following_matches[0]
        results.append((closest_following_verilog, listing, "after"))

# Определите имя файла для сохранения результатов
output_file = 'datasets_finetune/output_Цифровой_синтез.txt'

with open(output_file, 'w', encoding='utf-8') as file:
    for verilog_code, listing_description, position in results:
        file.write(f"Блок кода Verilog ({position}):\n")
        file.write(verilog_code)
        file.write("\nОписание листинга или примера:\n")
        file.write(listing_description)
        file.write("\n-----\n\n")