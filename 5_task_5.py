# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Pretask_5.txt', 'w+') as f:
    try:
        number = input('Введите числа через пробел \n')
        data = f.writelines(number)
        number_2 = number.split()
        print(sum(map(int, number_2)))
    except ValueError:
        print('Данные введены некорректно!!!')