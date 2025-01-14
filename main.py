import random

import colorgram
from turtle import Turtle, Screen
import turtle as t
# rgb_colors=[]
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
tim = t.Turtle()
tim.color("white")
tim.setx(-200)
tim.sety(-200)
tim.speed(0)


def drawing():
    for _ in range(10):
        # for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()


for i in range(9):
    drawing()
    tim.sety(tim.ycor() + 50)
    tim.setx(-200)

screen = Screen()
screen.exitonclick()