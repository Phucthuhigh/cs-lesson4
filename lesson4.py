# for i in range(11):
#     print(i, end=' ')

# for i in range(100, 106):
#     print(i, end=' ')

# for i in range(2, 10):
#     print(9 - i + 2, end=' ')

# for i in range(20):
#     if i % 3 == 0:
#         print(i)

# n = int(input())

# for i in range(n + 1):
#     print(i, end=' ')

# n = int(input())
# count = 0

# while n != 0:
#     count += 1
#     n //= 10
# print(count)

# n = int(input())
# s = 0

# for i in range(1, n + 1):
#     s += i**2

# print(s)

# n = int(input())
# s = 0

# for i in range(1, n + 1):
#     s += i/(i+1)

# print(round(s, 3))

# n = int(input())

# for i in range(1, n + 1):
#     if (n % i == 0):
#         print(i, end=' ')

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("#", end=' ')
#     print("\n", end='')

# n = input()

# for i in range(len(n)):
#     print(n[len(n)-i-1], end='')

# import math

# def isPrime(n):
#     if n < 2:
#         return False
#     if n % 2 == 0 and n != 2:
#         return False
#     if n == 2:
#         return True
#     for i in range(3, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# n = int(input())

# for i in range(n+1):
#     if isPrime(i):
#         print(i, end=' ')

# def isFinishing(n):
#     if n <= 0:
#         return False
#     s = 0
#     for i in range(1, n):
#         if n % i == 0:
#             s += i
#     if s == n:
#         return True
#     return False

# n = int(input())

# print(isFinishing(n))

# import turtle

# turtle.Screen()

# pen = turtle.Turtle()

# pen.pendown()
# for i in range(10,210,10):
#     print(i)
#     pen.circle(i,180)

# turtle.done()

# import turtle

# turtle.Screen()

# pen = turtle.Turtle()

# pen.pendown()

# n = int(input())
# while n <= 2:
#     n = int(input())
    
# angle = ((n-2)*180)/n
# for i in range(n):
#     pen.forward(n*20)
#     pen.left(180 - angle)

# turtle.done()

# def sumDigits(input):
#     if input < 0:
#         return 0
#     s = 0
#     while input != 0:
#         s += (input%10)
#         input //= 10
#     return s

# count = 0
# i = 1000
# while count < 10:
#     if sumDigits(i) == 9:
#         print(i, end=' ')
#         count += 1
#     i += 1

# def sumDigits(input):
#     if input < 0:
#         return 0
#     s = 0
#     while input != 0:
#         s += (input%10)
#         input //= 10
#     return s

# n = int(input())

# print(sumDigits(n))

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

# n = int(input())

# if n == 0:
#     print(1)
# elif n < 0:
#     print("Invalid")
# else:
#     s = 1
#     for i in range(1,n+1):
#         s *= i
#     print(s)

# n = int(input())

# while n <= 0:
#     n = int(input())
# print("Thank you")

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("#", end=' ')
#     print("\n", end='')