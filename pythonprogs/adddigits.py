def addDigits(num):
    while(num >= 10):
        temp = 0
        while(num > 0):
            temp += num % 10
            num = num // 10
        num = temp
    return num

a = addDigits(405)
print (a)


def adddigits(num):
    while(num >= 10):
        temp = num // 10 + num % 10
        num = temp
    return num

ans = adddigits(348)
print(ans)