
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')
colors = ['pink', 'orange', 'yellow', 'green', 'blue']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_id in range(0, 5):
    tur = Turtle(shape='turtle')
    tur.penup()
    tur.color(colors[turtle_id])
    tur.goto(x=-230, y=y_position[turtle_id])
    all_turtles.append(tur)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle in all_turtles:
            if turtle.xcor() > 230:
                race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()
