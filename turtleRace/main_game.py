from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter one of the rainbow color:"
                                                          "\n(red, orange, yellow, green, blue or purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while True:
    if user_bet not in colors:
        user_bet = screen.textinput(title="Wrong choice!!!!",
                                    prompt="You have to enter one of the rainbow color:"
                                           "\n(red, orange, yellow, green, blue or purple)")
    elif user_bet in colors:
        break

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle wins the race!")
            else:
                print(f"You've lost. The {winning_color} turtle wins the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()