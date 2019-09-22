import turtle
import math
import random
width=2000
height=1000
turtle.speed(0)
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width,height)

turtle.penup()
radius=500
turtle.setpos(radius,-30)
turtle.pendown()
turtle.pencolor("red")
turtle.left(90)
colours=["#e6194b","#f58231","#ffe119","#bcf60c","#3cb44b","#46f0f0","#4363d8","#911eb4","#f032e6"]
for i in range(1000):
    turtle.pencolor(colours[math.floor(len(colours)*random.random())])
    turtle.pendown()
    turtle.write("SVEN IS A RUNT",font=("Arial", math.floor(8-(i)*7/1000), "normal"))
    turtle.penup()
    turtle.forward((radius*math.pi*2/100000*(1000-i)))
    #print(12.6/1000*(1000-i))
    turtle.left(3.6)
turtle.hideturtle()
turtle.getscreen().getcanvas().postscript(file='spiral.ps')
