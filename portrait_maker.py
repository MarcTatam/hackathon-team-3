from turtle import *
import random

t = Turtle()
screen = Screen()

t.hideturtle()

screen.colormode(255)
t.penup()
t.left(90)
t.forward(250)
t.right(90)
t.pendown()
t.pencolor(241, 187, 151) #face
t.circle(100)
t.penup()

t.left(70)
t.forward(140)
t.pencolor(44,45,39)
t.pendown()
t.dot(None,'blue')
t.penup()
t.left(110) #eyes
t.forward(90)
t.pendown()
t.dot(None,'blue')
t.penup()

t.left(95)
t.forward(75)
t.pencolor(166, 92, 81)
t.pendown()
t.left(60)
for i in range(1,30):       #mouth
    t.forward(4)
    t.left(2.5)
t.left(105)
t.penup()
t.forward(70)
t.pendown()
t.left(120)
t.forward(10)
for i in range(1,6):
    t.forward(2)
    t.left(10)              #nose
for i in range(1,54):
    t.forward(1)
    t.right(5)
for i in range(1,6):
    t.forward(2)
    t.left(10)
t.forward(10)
t.left(60)
t.penup()
t.forward(90)
t.right(30)
t.pencolor(90, 73, 53)
t.pendown()

for i in range(1,30):
    t.forward(8)
    t.right(119)
    t.forward(8)
    t.left(113.8)

t.right(105)
t.penup()
t.forward(155)
t.pendown()
t.pencolor(43, 46, 39)
t.left(35)
t.forward(400) #body
t.left(35)
t.forward(250) #leg `
t.right(180)
t.forward(250)
t.left(110)
t.forward(250) #leg 2
t.right(180)
t.forward(250)
t.left(35)
t.forward(200)
t.left(90)
t.forward(175)
t.right(180)
t.forward(350)
