from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet", prompt="Which turtle will win the race? Enter a rainbow colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
all_turtles = []


def turtle_instance(name, color, height):
    name = Turtle(shape="turtle")
    name.penup()
    name.goto(x=-230, y=height)
    name.color(colors[color])
    all_turtles.append(name)


turtle_instance("bev", 1, 100)
turtle_instance("tev", 0, 50)
turtle_instance("kev", 2, 0)
turtle_instance("lev", 3, -50)
turtle_instance("sev", 4, -100)
turtle_instance("nev", 5, -150)


if user_bet:
    start_race = True


while start_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            start_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lose! The The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

