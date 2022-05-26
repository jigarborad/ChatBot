import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MakeYour Bet", prompt="Guess Your Bet on color = ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_positions = [-90, -60, -30, 0, 30, 60, 90]
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setpos(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You Won")
            else:
                print(f"You Lost! {winning_color} turtle won")
            print("")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
