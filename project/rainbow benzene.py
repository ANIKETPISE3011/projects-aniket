#python program to draw
#Rainbow benzene
#using turtle programming

import turtle
colors= ['red', 'purple','blue','green','orange','yellow']
t= turtle.Pen()
turtle.speed(200)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
turtle.done()
