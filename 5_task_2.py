# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
f = open('Pretask_2.txt', 'r')
qty_word = [f'{num}. {" ".join(line.split())} - {len(line.split())} слов(а,о)' for num, line in enumerate(f, 1)]
print(f'Количество строк - {len(qty_word)}')
print(*qty_word, sep='\n')
f.close()