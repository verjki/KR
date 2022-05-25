
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

#print(substring_slice())