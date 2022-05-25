# Написать функцию calculate, которая принимает на вход текстовый файл
# содержащий строки следующего формата:
# Формат файла: арифметическая операция целое число #1 целое число #2
# Разделитель - 4 пробела
# Функция должна вернуть 1 строку. Строка содержит набор из чисел, разделенных запятой.
# После последнего числа запятая не ставится.
# Каждое число - результат операции: "результирующее целое число" = "целое число #1"
# применить "арифметическая операция" "целое число #2"

def calculate(f):
    f2 = open(f, 'r')
    results = []

    for line in f2.readlines():

        new_list = []
        list = line.split('    ')
        list[0], list[1] = list[1], list[0]
        for k in list:
            new_list.append(k)

        num1 = new_list[0]
        num2 = new_list[2]
        oper = new_list[1]
        if oper == '+':
            result = int(num1) + int(num2)
        elif oper == '-':
            result = int(num1) - int(num2)
        elif oper == '*':
            result = int(num1) * int(num2)
        elif oper == '//':
            if int(num1) < 0 or int(num2) < 0 or int(num2) == 0:
                return 'Для данной операции передаются положительные числа'
            else:
                result = int(num1) // int(num2)
        elif oper == '%':
            if int(num1) < 0 or int(num2) < 0 or int(num2) == 0:
                return 'Для данной операции передаются положительные числа'
            else:
                result = int(num1) % int(num2)
        elif oper == '**':
            if int(num1) < 0 or int(num2) < 0:
                return 'Для данной операции передаются положительные числа'
            else:
                result = int(num1) ** int(num2)
        results.append(str(result))
    results_str = ','.join(results)
    f2.close()
    return results_str
#print(calculate())

