from turtle import *
from colorsys import *
setposition(10, -10)
speed(0)
color('black')
bgcolor('black')
pensize(2)
h= 0
for i in range(30):
    for j in range(4):
        color(hsv_to_rgb(h, 1, 1))
        h +=0.3
        circle(40+j*5, 90)
        forward(250)
        left(90)
        right(10)
        hideturtle()
