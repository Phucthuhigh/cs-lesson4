import turtle

turtle.Screen()

pen = turtle.Turtle()

pen.pendown()
for i in range(10,210,10):
    print(i)
    pen.circle(i,180)

turtle.done()