##roman numerals to arabic

def R2A(char):
    if char ==  'M':
        return 1000
    elif char == 'D':
        return 500
    elif char == 'C':
        return 100
    elif char == 'L':
        return 50
    elif char == 'X':
        return 10
    elif char == 'V':
        return 5
    elif char == 'I':
        return 1

def convert(roman):
    total = 0
    listroman = list(roman)
    for i in range(0,len(listroman)):
        listroman[i] = R2A(listroman[i])
    for i in range(len(listroman)):
        total += listroman[i]
        try:
            if listroman[i+1] > listroman[i]:
                total -= 2 * listroman[i]
        except:
            pass
    return total

print(convert('MCXLV'))
