import random
import turtle
from turtle import Turtle,Screen
screen=Screen()
# screen.bgpic("racetrack.jpg")
is_game_on=False
user_bet=screen.textinput(title="Make your bet.",prompt="Which turtle will win the race ? Enter a color: ")
timmy=Turtle()
timmy.shape("turtle")
color=["violet","blue","green","yellow","orange","red"]

screen.setup(width=500 , height=500)
timmy.penup()
jimmy=Turtle()
jack=Turtle()
nanny=Turtle()
tim=Turtle()
sam=Turtle()
pos_y=[-200,-100,0,100,200]
items=[tim,sam,nanny,jack,jimmy]
tim.penup()
sam.penup()
nanny.penup()
jack.penup()
jimmy.penup()
counter=0
# tim.setpos(-200,pos_y[0])
# sam.setpos(-200,pos_y[1])
# nanny.setpos(-200,pos_y[2])
# jack.setpos(-200,pos_y[3])
# jimmy.setpos(-200,pos_y[4])

for item in items:
    item.shape("turtle")
    item.color(color[counter])
    item.setpos(-200,pos_y[counter])
    counter+=1

timmy.hideturtle()
line_man=Turtle()
line_man.shapesize(0.1, 0.1, 1)
line_man.shape("square")
line_man.color("black")
line_man.penup()
line_man.goto(230,-230)
line_man.left(90)
line_man.pendown()
line_man.forward(460)


if(user_bet):
    is_game_on=True

while is_game_on:
    for turtl in items:
        turtl.forward(random.randint(0,10))
        if(turtl.xcor()>230):
            winner=turtl.pencolor()
            if(winner==user_bet.lower()):
                print(f"You have Won ! . The {winner} color turtle is the winner.")
            else:
                print(f"You have Lost ! . The {winner} color turtle is the winner.")
            is_game_on=False
print("\n\n\nThank You !!!")

screen.exitonclick()
