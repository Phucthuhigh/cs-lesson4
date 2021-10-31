def sumDigits(input):
    if input < 0:
        return 0
    s = 0
    while input != 0:
        s += (input%10)
        input //= 10
    return s

count = 0
i = 1000
while count < 10:
    if sumDigits(i) == 9:
        print(i, end=' ')
        count += 1
    i += 1