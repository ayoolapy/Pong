import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
r_paddle.color("blue")
l_paddle = Paddle((-380, 0))
l_paddle.color("green")
ball = Ball((0, 0))
score = Score()

line = Turtle()
line.goto(y=-300, x=0)
line.setheading(90)
line.pencolor("white")
line.forward(600)
line.goto(0, 0)
line.shape("circle")


screen.listen()
screen.onkeypress(r_paddle.up, key="Up")
screen.onkeypress(r_paddle.down, key="Down")
screen.onkeypress(l_paddle.up, key="w")
screen.onkeypress(l_paddle.down, key="s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 395:
        score.l_point()
        ball.reset_position()

    elif ball.xcor() < -395:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
