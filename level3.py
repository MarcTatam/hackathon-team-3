""" Hackathon - Level 3 """

def oddish_evenish(x):
    listnum = list(str(num))
    total = 0
    for number in listnum:
        total += int(number)
    if total % 2 == 0:
        return 'Evenish'
    else:
        return 'Oddish'

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return Oddish
    print(oddish_evenish(1190))
