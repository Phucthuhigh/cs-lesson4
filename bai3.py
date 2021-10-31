# Cách 1:
# def giaithua(n):
#     if n < 0:
#         return -1
#     if n == 0 or n == 1:
#         return 1
#     else: 
#         return n*giaithua(n-1)

# n = int(input())

# if giaithua(n) == -1:
#     print("Invalid")
# else:
#     print(giaithua(n))

# Cách 2:
n = int(input())

if n == 0:
    print(1)
elif n < 0:
    print("Invalid")
else:
    s = 1
    for i in range(1,n+1):
        s *= i
    print(s)