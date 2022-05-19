from re import L, T
from tkinter import CENTER, font
import turtle

nigga = turtle.Screen()
nigga.title("Pong by @FAISAL!! LETSGOO")
nigga.bgcolor("green")
nigga.setup(width=800, height=600)
nigga.tracer(0)

#SCORE!!!
score1 = 0
score2 = 0


#Paddles and BALLS 0_0
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("purple")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)


paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("purple")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)


balls0_0 = turtle.Turtle()
balls0_0.speed(0)
balls0_0.shape("circle")
balls0_0.color("brown")
balls0_0.penup()
balls0_0.goto(0,0)
balls0_0.dx = 0.09
balls0_0.dy = 0.09

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write((f"Player 1: {score1} Player 2: {score2}"), align="center", font=("courier", 24, "normal"))


def paddle1_movement_up():
	y = paddle1.ycor()
	y += 20
	paddle1.sety(y)


def paddle1_movement_down():
	y = paddle1.ycor()
	y -= 20
	paddle1.sety(y)


def paddle2_movement_up():
	y = paddle2.ycor()
	y += 20
	paddle2.sety(y)


def paddle2_movement_down():
	y = paddle2.ycor()
	y -= 20
	paddle2.sety(y)


#keyboard bindings
nigga.listen()
nigga.onkeypress(paddle1_movement_up,"w")
nigga.onkeypress(paddle1_movement_down, "s")

nigga.onkeypress(paddle2_movement_up,"Up")
nigga.onkeypress(paddle2_movement_down, "Down")



#Main loop 
while True:
	nigga.update()

	#ball movement
	balls0_0.setx( balls0_0.xcor() + balls0_0.dx )
	balls0_0.sety( balls0_0.ycor() + balls0_0.dy )

	#ball bounce
	if balls0_0.ycor() > 290:
		balls0_0.sety(290)
		balls0_0.dy *= -1

	if balls0_0.ycor() < -290:
		balls0_0.sety(-290)
		balls0_0.dy *= -1

	if balls0_0.xcor() > 390:
		balls0_0.goto(0,0)
		balls0_0.dx *= -1
		score1 += 1
		pen.clear()
		pen.write((f"Player 1: {score1} Player 2: {score2}"), align="center", font=("courier", 24, "normal"))


	if balls0_0.xcor() < -390:
		balls0_0.goto(0,0)
		balls0_0.dx *= -1
		score2 += 1
		pen.clear()
		pen.write((f"Player 1: {score1} Player 2: {score2}"), align="center", font=("courier", 24, "normal"))


	#ball and stick collisions

	if (balls0_0.xcor() > 340 and balls0_0.xcor() < 350) and (balls0_0.ycor() < paddle2.ycor() + 50 and balls0_0.ycor() > paddle2.ycor() -50):
		balls0_0.setx(340)
		balls0_0.dx *= -1.03

	if (balls0_0.xcor() < -340 and balls0_0.xcor() > -350) and (balls0_0.ycor() < paddle1.ycor() + 50 and balls0_0.ycor() > paddle1.ycor() -50):
		balls0_0.setx(-340)
		balls0_0.dx *= -1.03