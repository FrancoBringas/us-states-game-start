import csv
import turtle
from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S.States Game")
screen.screensize(300,300)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
remainig_states = 50
states_to_learn = []
for row in data:
    states_to_learn.append(row[0])
while remainig_states > 0:
    answer_state = screen.textinput(title="guess the state", prompt=f"remaining states {remainig_states}  what's another state's name?")
    with open("50_states.csv") as data_file:
        data = csv.reader(data_file)
        tim = Turtle()
        for row in data:
            states_to_learn.append(row[0])
            if row[0] == answer_state. capitalize():
                states_to_learn.remove(row[0])
                x = int(row[1])
                y = int(row[2])
                tim.penup()
                tim.color("black")
                tim.goto(x,y)
                tim.write(answer_state)
                remainig_states -= 1
            elif answer_state == "salir":
                remainig_states = 0
print(states_to_learn)
screen.exitonclick()
