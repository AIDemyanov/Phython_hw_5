# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

f = open('Pretask_3.txt', 'r')
data = f.read()
data = data.split('\n')
persons = []
income = []
for el in data:
    el = el.split()
    if int(el[1]) < 20000:
        persons.append(el[0])
    income.append(el[1])
print(f'Сотрудники, имеющие оклад менее 20 тыс. {persons}')
print(f'Средний оклад по фирме {sum(map(int, income)) / len(income)}')
f.close()