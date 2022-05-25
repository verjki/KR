import re
def is_palindrome(string):
    string2 = re.sub('[!@#$\n-.,]', '',string)
    string2 = ''.join((x for x in string2 if not x.isdigit()))



    s = string2.upper()
    li_str = []
    for k in s:
        if s.isalpha() == True:
            li_str.append(k)
    l = 0
    r = len(li_str) - 1
    while l < r:
        if li_str[l] != li_str[r]:
           return 'NO'
           break
        elif li_str[l] == li_str[r]:
            return'YES'
            break
        else:
            l = l + 1
            r = r - 1
#print(is_palindrome(""))
