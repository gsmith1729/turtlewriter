import turtle
import random
import math
import time
import winsound
#link to happy music
sfhappy=r"happyMusic.wav"
#link to scary music
sfscary=r"scareSoundEffect.wav"
def runt():
    turtle.clear()
    winsound.PlaySound(sfscare,winsound.SND_ASYNC | winsound.SND_ALIAS )
    time.sleep(1.2)
    turtle.penup()
    turtle.setpos(-420,-50)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.write("SVEN IS A RUNT",font=("Chiller", 100, "normal"))
    time.sleep(9.4)
    winsound.PlaySound(None, winsound.SND_PURGE)
winsound.PlaySound(sfhappy,winsound.SND_ASYNC | winsound.SND_ALIAS )
width=2000
height=1000
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width,height)
turtle.hideturtle()
turtle.speed(10)
turtle.pendown()
turtle.pencolor("white")
turtle.fillcolor("white")
colours=["#e6194b","#f58231","#ffe119","#bcf60c","#3cb44b","#46f0f0","#4363d8","#911eb4","#f032e6"]
start=time.time()
def chin(x,y):
    turtle.pencolor(colours[math.floor(len(colours)*random.random())])
    turtle.write("SVEN IS A RUNT",font=("Arial", 3+math.floor(60*(random.random()**5)), "normal"))
    turtle.penup()
    turtle.setpos(width*random.random()-width*1.1/2,height*random.random()-height/2)
    turtle.pendown()

intervene=30
#turtle.onclick(chin)
turtle.penup()
radius=500
turtle.setpos(radius,-10)
turtle.pendown()
turtle.pencolor("red")
turtle.left(90)
i=0
while(time.time()-start<intervene):#i<1000):
    turtle.pencolor(colours[math.floor(len(colours)*random.random())])
    turtle.pendown()
    turtle.write("SVEN IS A RUNT",font=("Arial", math.floor(8-(i)*7/1000), "normal"))
    turtle.penup()
    turtle.forward((radius*math.pi*2/100000*(1000-i)))
    #print(12.6/1000*(1000-i))
    turtle.left(3.6)
    #uncomment for random word placement and comment above
    #chin(1,1)
    i+=1
turtle.hideturtle()   
winsound.PlaySound(None, winsound.SND_PURGE)    
runt()





