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
print(bin_search([2,5,7,9,11,17,222],11))

