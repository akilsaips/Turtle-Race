from turtle import *
from random import *

game_is_on = False

screen = Screen()
screen.setup(width=500, height=400)
userbet = screen.textinput(title="Make a bet", prompt="Enter a color: ")

colors = ["red", "blue", "green", "cyan", "purple", "pink"]
y_p = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle in range(0, 6):
    sam = Turtle(shape="turtle")
    sam.color(colors[turtle])
    sam.penup()
    sam.goto(x=-230, y=y_p[turtle])
    turtles.append(sam)

if userbet:
    game_is_on = True

while game_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_is_on = False
            wincolor = turtle.pencolor()
            if userbet == wincolor:
                print(f"You've won! {wincolor} is the correct answer.")
            else:
                print(f"You've lost! {wincolor} is the correct answer.")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
