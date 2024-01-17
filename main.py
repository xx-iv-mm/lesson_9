import re

# Exercise 1
import os
import platform

print("Operating system: ", platform.system())
print("Current directory: ", os.getcwd())
if not os.path.exists("data_txt"):
    os.mkdir("data_txt")
if not os.path.exists("data_rar"):
    os.mkdir("data_rar")
if not os.path.exists("data_pdf"):
    os.mkdir("data_pdf")
sum_txt = 0
sum_rar = 0
sum_pdf = 0
txt_size = 0
rar_size = 0
pdf_size = 0
for filename_txt in os.listdir():
    if ".txt" in filename_txt:
        txt_size += os.path.getsize(filename_txt)
        os.replace(filename_txt, f"data_txt/{filename_txt}")
        sum_txt += 1
for filename_rar in os.listdir():
    if ".rar" in filename_rar:
        rar_size += os.path.getsize(filename_rar)
        os.replace(filename_rar, f"data_rar/{filename_rar}")
        sum_rar += 1
for filename_pdf in os.listdir():
    if ".pdf" in filename_pdf:
        pdf_size += os.path.getsize(filename_pdf)
        os.replace(filename_pdf, f"data_pdf/{filename_pdf}")
        sum_pdf += 1
print(f"{sum_txt} файл/-ов перемещено в папку data_txt общим размером - {txt_size} кб")
print(f"{sum_rar} файл/-ов перемещено в папку data_rar общим размером - {rar_size} кб")
print(f"{sum_pdf} файл/-ов перемещено в папку data_pdf общим размером - {pdf_size} кб")
os.rename(f"data_txt/{filename_txt}", "data_txt/renamed.txt")
print(f"Файл {filename_txt} был переименован в renamed.txt")

# Exercise 2
# s = ('Подсудимая Эверт-Колокольцева Елизавета Александровна\n'
#      'в судебном заседании вину инкриминируемого\n'
#      'правонарушения признала в полном объёме и суду показала,\n'
#      'что 14 сентября 1876 года, будучи в состоянии алкогольного\n'
#      'опьянения от безысходности, в связи с состоянием здоровья\n'
#      'позвонила со своего стационарного телефона в полицию,\n'
#      'сообщив о том, что у неё в квартире якобы заложена бомба.\n'
#      'После чего приехали сотрудники полиции, скорая\n'
#      'и пожарные, которым она сообщила, что бомба — это она.'
#      )
# print(re.sub(r'[А-ЯЁ]\w*' r'(?:-[А-ЯЁ]\w*)?' r'(?: [А-ЯЁ]\w*){2}', 'N', s))

# Exercise 3
# def most_common_word(lines):
#     result_lines = {}
#     for line in lines:
#         data = {}
#         words = line.split()
#
#         for word in words:
#             if not word in data:
#                 data[word] = 1
#             else:
#                 data[word] = data[word] + 1
#
#         if data:
#             most_common = max(data, key=data.get)
#             count = data[most_common]
#             result_lines[most_common] = count
#
#     return result_lines
#
#
# def process_file(input_file, output_file):
#     with open(input_file, 'r') as file:
#         lines = file.readlines()
#
#     with open(output_file, 'w') as output:
#         result_lines = most_common_word(lines)
#         for most_common, count in result_lines.items():
#             output.write(f"Самое частое слово в строке: {most_common},\nКоличество повторений: {count}\n\n")
#
#
# if __name__ == "__main__":
#     input_file_path = "lesson9_3.txt"
#     output_file_path = "output.txt"
#
#     process_file(input_file_path, output_file_path)

# Exercise 4
# with open(input(), encoding='utf-8') as words_file, open('stop_words.txt', encoding='utf-8') as file:
#     stop_words = file.read().split()
#     for s in words_file:
#         for x in stop_words:
#             while x in s.lower():
#                 index = s.lower().index(x)
#                 s = s[:index] + '*' * len(x) + s[index + len(x):]
#         print(s.split())

# Exercise 5
# def print_low_grades(file_path):
#     with open(file_path, 'r', encoding='') as file:
#         for line in file:
#             data = line.split()
#             name = f"{data[0]} {data[1]}"
#             grade = int(data[2])
#
#             if grade < 3:
#                 print(f"{name}: {grade} балла")
#
# # Пример вызова функции
# file_path = 'lesson9_5.txt'
# print_low_grades(file_path)

# Exercise 6
# with open("lesson9_6.txt", encoding='utf-8') as file:
#     s = 0
#     k = '0'
#     for i in file.read():
#         if i.isdigit():
#             k += i
#         else:
#             s += int(k)
#             k = '0'
#     print(f"Сумма цифр в строке равна:  {s}")

# Exercise 7
# def ceasar_encode(letter, shift):
#     if letter.isalpha():
#         number = ord(letter) + shift % 25
#         if number > 122 or 90 < number < 97:
#             number -= 25
#         return chr(number)
#     return letter
#
#
# i = 0
# with open('lesson9_7.txt') as text:
#     for line in text:
#         i += 1
#         for l in line:
#             print(ceasar_encode(l, i), end='')
