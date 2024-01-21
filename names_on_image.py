from turtle import Turtle
FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"

class NameTag():
    def __init__(self, name, x, y):
        name_tag = Turtle()
        name_tag.penup()
        name_tag.hideturtle()
        name_tag.color("black")
        name_tag.goto(x, y)
        name_tag.write(name, align=ALIGNMENT, font=FONT)



