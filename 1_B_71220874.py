# F
import turtle
l = turtle.Turtle()
l.penup()
l.setpos(-180,80)
l.pendown()

l.pensize(40)
l.pencolor("blue")

l.forward(100)
l.backward(100)
l.right(90)
l.forward(100)

l.left (90)
l.forward (100)
l.backward (100)

l.right (90)
l.forward (100)

# 8
import turtle
l = turtle.Turtle()
l.pensize (30)
l.color ("blue")

l.penup()
l.setpos (-20,80)
l.pendown ()

for i in range (4):
    l.forward(50)
    l.right (90)

# s
import turtle 
l = turtle.Turtle()
l.pensize (30)
l.color ("blue")

l.penup ()
l.setpos (250,100)
l.pendown ()

l.forward (30)
l.backward (30)

l.circle (-70,-185)
l.circle (70,-250)