##roman numerals to arabic
""" Hackathon - Level 5 """

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
        
def convert(numeral):
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

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 1145
    print(convert('MCXLV'))

