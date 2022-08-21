 # Steps to be followed
"""
    Step 1) Create two paddles A and B on the lest and right side of the screen.
    Step 2) Create a ball.
    Step 3) Create an event to move the paddle vertically on pressing a certain key.
    Step 4) Create the function to update the score after each player missing a collision.
    """
# Importing required library

import time
import turtle
import random
import pygame.mixer as pm
import os

pm.init()
s = 'sound'
jump = pm.Sound(os.path.join(s, 'jump.mp3'))
start = pm.Sound(os.path.join(s, 'start.mp3'))
congratulations = pm.Sound(os.path.join(s, 'cong.mp3'))
wall = pm.Sound(os.path.join(s, 'wall.wav'))

def create_paddle():
    pad = turtle.Turtle()
    pad.speed(0)
    pad.color("black")
    pad.shape("square")
    pad.shapesize(stretch_wid=6, stretch_len=1)
    pad.penup()
    return pad

def game():
    screen.clear()
    screen.bgcolor("yellow")
    screen.bgpic("naruto2.png")
    # Creating Left paddle
    left_pad = create_paddle()
    left_pad.goto(-400, 0)

    # Creating Right paddle
    right_pad = create_paddle()
    right_pad.goto(400, 0)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    ball.goto(0, 0)
    a = random.choice([1,-1])
    b = random.randrange(1, 11)/100
    ball.dx = a*130
    ball.dy = -a*(b+1)*120

    # Initialize Score
    left_score = 0
    right_score = 0

    # Displays the score of both players
    sketch = turtle.Turtle()
    sketch.speed(0)
    sketch.penup()
    sketch.hideturtle()
    sketch.color("brown")
    sketch.goto(-490, 260)
    sketch.write("             {}".format(str(left_score).zfill(2)),font=("Courier", 24, "bold"))
    player_1 = turtle.Turtle()
    player_1.speed(0)
    player_1.penup()
    player_1.hideturtle()
    player_1.color("brown")
    player_1.goto(-490, 260)
    player_1.write("Player One :   /30",font=("Courier", 24, "bold"))

    player_1.goto(490 - len("Player Two :  00/10") * 18, 260)
    player_1.write("Player Two :   /30",font=("Courier", 24, "bold"))

    sketch_1 = turtle.Turtle()
    sketch_1.speed(0)
    sketch_1.penup()
    sketch_1.hideturtle()
    sketch_1.color("brown")
    sketch_1.goto(490 - len("Player Two : 00/10") * 18, 260)
    sketch_1.write("            {}".format(str(right_score).zfill(2)),font=("Courier", 24, "bold"))

    # Functions to move Paddle vertically
    def paddle_1_up():
        y = left_pad.ycor()
        if(y <= 230):
            y += 25
        left_pad.sety(y)


    def paddle_1_down():
        y = left_pad.ycor()
        if(y >= -230):
            y -= 25
        left_pad.sety(y)


    def paddle_2_up():
        y = right_pad.ycor()
        if (y <= 230):
            y += 25
        right_pad.sety(y)


    def paddle_2_down():
        y = right_pad.ycor()
        if (y >= -230):
            y -= 25
        right_pad.sety(y)

    # Keyboard binding
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")

    global current_time
    current_time = 0
    prev_time = time.clock()
    global count
    count = 1
    while True:
        screen.tracer(1, 0)
        current_time = time.clock()
        dt = abs(current_time - prev_time)
        prev_time = current_time

        if(current_time > 10*count and current_time <= 300):
            ball.dx += ball.dx*0.1
            ball.dy += ball.dy*0.1
            count += 1
        ball.sety(ball.ycor() + ball.dy*dt)
        ball.setx(ball.xcor() + ball.dx*dt)

        # Checking border
        if (ball.ycor() > 280):
            pm.Sound.play(wall)
            ball.sety(280)
            ball.dy *= -1

        if (ball.ycor() < -280):
            pm.Sound.play(wall)
            ball.sety(-280)
            ball.dy *= -1

        if (ball.xcor() > 500):
            ball.setx(0)
            ball.sety(0)
            a = random.choice([1, -1])
            b = random.randrange(1, 11) / 100
            ball.dy = a * (b + 1) * ball.dy
            left_score += 1
            sketch.clear()
            sketch_1.clear()
            sketch.write("             {}".format(str(left_score).zfill(2)),
                         font=("Courier", 24, "bold"))
            sketch_1.write("            {}".format(str(right_score).zfill(2)),
                           font=("Courier", 24, "bold"))

        if (ball.xcor() < -500):
            ball.goto(0, 0)
            a = random.choice([1, -1])
            b = random.randrange(1, 11) / 100
            ball.dy = a * (b+1) * ball.dy
            right_score += 1
            sketch.clear()
            sketch_1.clear()
            sketch.write("             {}".format(str(left_score).zfill(2)),
                         font=("Courier", 24, "bold"))
            sketch_1.write("            {}".format(str(right_score).zfill(2)),
                           font=("Courier", 24, "bold"))

        # Paddle ball collision
        if (ball.xcor() >= 380 and ball.xcor() <= 390 and (
                ball.ycor() < right_pad.ycor() + 68 and ball.ycor() > right_pad.ycor() - 68)):
            pm.Sound.play(jump)
            ball.setx(380)
            ball.dx *= -1

        if (ball.xcor() <= -380 and ball.xcor() >= -390 and (
                ball.ycor() < left_pad.ycor() + 68 and ball.ycor() > left_pad.ycor() - 68)):
            pm.Sound.play(jump)
            ball.setx(-380)
            ball.dx *= -1

        current_time = time.clock()
        if(left_score == 30 or right_score == 30):
            break

    screen.clear()
    screen.bgcolor("aqua")
    screen.bgpic("congrat.png")

    enter.color("Red")
    enter.goto(0, -100)
    if (left_score > right_score):
        pm.Sound.play(congratulations)
        enter.write("Player One Wins ", align="center", font=("Courier", 24, "bold"))
    if (left_score < right_score):
        pm.Sound.play(congratulations)
        enter.write("Player Two Wins ", align="center", font=("Courier", 24, "bold"))

    enter.color("brown")
    enter.goto(0, 250)
    enter.write("To Start again 'Enter' ", align="center", font=("Courier", 24, "bold"))
    enter.goto(0, 200)
    enter.write("To Quit the RasenPong game press 'Esc' ", align="center", font=("Courier", 24, "bold"))


def start_game():
    game()


def end_game():
    screen.bye()


def game_loop():
    pm.Sound.play(start)
    while True:
        screen.listen()
        screen.onkeypress(start_game, "Return")
        screen.onkeypress(end_game, "Escape")
        screen.update()


if __name__ == '__main__':
    # Creating Screen

    screen = turtle.Screen()
    screen.title("Rasenpong")
    screen.bgcolor("aqua")
    screen.bgpic("rasen.png")
    screen.setup(width=1000, height=600)
    enter = turtle.Turtle()
    enter.color("brown")
    enter.speed(0)
    enter.penup()
    enter.hideturtle()
    enter.goto(0, 250)
    enter.write("Welcome To Konoha Village", align="center", font=("Courier", 24, "bold"))
    enter.goto(0, 50)
    enter.write("To Start the RasenPong game press 'Enter' ", align="center", font=("Courier", 24, "bold"))
    enter.goto(0, 0)
    enter.write("To Quit the RasenPong game press 'Esc' ", align="center", font=("Courier", 24, "bold"))
    game_loop()

