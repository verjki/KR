
#l = input('Введите числа, разделяя пробелами: ')
#li = [int(i) for i in l.split(" ")]
def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))
#print(filter_even(li))

