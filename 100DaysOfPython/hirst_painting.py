import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# color_object = colorgram.extract('image.jpg', 30)
# color_list = []
#
#
# for i in range(len(color_object)):
#     rgb = color_object[i].rgb
#     color = (rgb[0], rgb[1], rgb[2])
#     color_list.append(color)
# print(color_list)
color_list = [(218, 234, 224), (141, 176, 206), (25, 32, 48), (28,
105, 156), (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195
), (182, 45, 84), (217, 60, 85), (226, 80, 44), (195, 129, 168), (54, 167, 116), (29, 61
, 115), (108, 181, 91), (109, 99, 88), (2, 102, 119), (193, 187, 47), (241, 204, 1), (19
, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186), (150, 207, 222), (234, 169,
 160), (184, 186, 210), (115, 38, 37)]


hirst = Turtle()
screen = Screen()
turtle.colormode(255)
hirst.penup()
hirst.hideturtle()
hirst.setposition(-300, 300)

for i in range(10):
    for n in range(10):
        hirst.dot(15, random.choice(color_list))
        hirst.forward(45)
    hirst.setposition(-300, hirst.position()[1]-45)


screen.exitonclick()
