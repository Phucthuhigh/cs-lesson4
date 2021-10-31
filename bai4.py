def sumDigits(input):
    if input < 0:
        return 0
    s = 0
    while input != 0:
        s += (input%10)
        input //= 10
    return s

n = int(input())

print(sumDigits(n))