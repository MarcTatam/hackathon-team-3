##oddish vs evenish

def oddish_evenish(num):
    listnum = list(str(num))
    total = 0
    for number in listnum:
        total += int(number)
    if total % 2 == 0:
        return 'Evenish'
    else:
        return 'Oddish'


print(oddish_evenish(1190))
