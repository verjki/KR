import json

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
#print(decode_ch('NOTiFICaTiON'))