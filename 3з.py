#l = input('Введите числа, разделяя пробелами: ')
#li = [int(i) for i in l.split(" ")]
def square(li):
  square_list = list(map(lambda x: x**2, li))
  return square_list
#print(square(li))