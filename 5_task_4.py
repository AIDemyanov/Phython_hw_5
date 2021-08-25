# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translate_number = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('Pretask_4_new.txt', 'w', encoding='utf-8') as file_new:
    with open('Pretask_4.txt', 'r', encoding='utf-8') as file_old:
        file_new.write(str([line.replace(line.split()[0], translate_number.get(line.split()[0])) for line in file_old]))