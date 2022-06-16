import re
import numpy
import json
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

#2
def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))

#3

def square(li):
  square_list = list(map(lambda x: x**2, li))
  return square_list

#4

def bin_search(li, element):
    li.sort()
    mid = len(li) // 2
    low = 0
    high = len(li) - 1
    while li[mid] != int(element) and low <= high:
        if int(element) > li[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return -1

    else:
        return mid
#5
def is_palindrome(string):
    string2 = ''.join(filter(lambda x: x.isalpha(), string))
    s = string2.upper()
    l = 0
    r = len(s) - 1
    while l != len(s) // 2:
        if s[l] != s[r]:
            return "NO"
        l += 1
        r -= 1
    return "YES"
#6
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

#7
def substring_slice(a, b):
    f1 = open(a, 'r')
    f2 = open(b, 'r')
    result = []
    for i in f1.readlines():
        slice = f2.readline().split()
        num1 = int(slice[0])
        num2 = int(slice[1])
        string_slice = i[num1:num2+1]
        result.append(string_slice)
    results = ' '.join(result)
    f2.close()
    f1.close()
    return results

#8

def decode_ch(string_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
    result = ''
    element = ''
    l = len(string_of_elements)
    for x in range(l):
        element += string_of_elements[x]
        if x + 1 == len(string_of_elements) or string_of_elements[x + 1].isupper():
            if element in periodic_table :
                result += periodic_table.get(element)
                element = ''
            else:
                result += 'Неверно указаны элементы'
    return result

#9

class Student:

    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.grades = grades

    def greeting(self):
        return 'Hello, I am Student', self

    def mean_grade(self):
        mean = numpy.average(self.grades)
        return mean

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, second):
        return f'{self.name} is friends with {second.name}'

    def __str__(self):
        return self.fullname

#10
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
