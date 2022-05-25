#li = list(map(int,input('Введите элементы списка через пробел: ').split(" ")))
#li = sorted(li)
#element = int(input('Искомый элемент: '))
def bin_search(li, element):
    if element in li:
        elem_index = li.index(element)
        return elem_index
    else:
        return -1
#print(bin_search(li,element))

