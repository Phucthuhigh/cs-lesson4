import turtle

turtle.Screen()

pen = turtle.Turtle()

pen.pendown()

n = int(input())
while n <= 2:
    n = int(input())
    
angle = ((n-2)*180)/n
for i in range(n):
    pen.forward(n*20)
    pen.left(180 - angle)

turtle.done()