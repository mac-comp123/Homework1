"""
Draws six circles, centered on the origin, each a different color.
Assumption: the number of colors in the turtle colors list is at least
as long as the number of rings.
"""


import turtle
import math

scr = turtle.Screen()
turt = turtle.Turtel()

scr.bgcolor("seashell")

tColors = ["light salmon", "light sky blue", "pale green", "light coral", "pale turquoise", "plum"]

turt.width(5)
numRings = 6

for i in range(numRings):
    turt.color(tColors[0])
    radius = 40 * (i + 1)

    
    turt.up()
    turt.forward(radius)
    turt.down()
    
    turt.left(90)
    turt.circle(i)
    turt.right(60)
    
    turt.up
    turt.backward(radius)
    turt.down()

scr.exitonclick()
