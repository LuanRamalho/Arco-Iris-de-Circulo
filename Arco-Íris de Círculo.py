from turtle import *
import turtle

z = turtle.Screen()
speed(0)
hideturtle()
bgcolor('black')
pensize(5)
penup()

for m in range(36):
    fd(350)
    pendown()
    color('red')
    circle(21)
    penup()
    bk(350)
    rt(10)

for w in range(36):
    fd(300)
    pendown()
    color('orange')
    circle(18)
    penup()
    bk(300)
    rt(10)

for u in range(36):
    fd(250)
    pendown()
    color('yellow')
    circle(15)
    penup()
    bk(250)
    rt(10)

for k in range(36):
    fd(200)
    pendown()
    color('lime')
    circle(12)
    penup()
    bk(200)
    rt(10)

for x in range(36):
    fd(150)
    pendown()
    color('deepskyblue')
    circle(9)
    penup()
    bk(150)
    rt(10)

for l in range(36):
    fd(100)
    pendown()
    color('blue')
    circle(6)
    penup()
    bk(100)
    rt(10)

for n in range(36):
    fd(50)
    pendown()
    color('magenta')
    circle(3)
    penup()
    bk(50)
    rt(10)

pendown()
for a in range(5):
    for Cir_colors in ['red' , 'orange' , 'yellow' , 'lime' , 'deepskyblue' , 'blue' , 'magenta' , 'white']:
        color(Cir_colors)
        circle(10)
        right(10)

z.exitonclick()


