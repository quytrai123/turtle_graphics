import turtle
a = turtle.Turtle()
a.shape("turtle")
a.speed(0)
a.getscreen().bgcolor("gray")
a.penup()
a.goto(-200,200)
a.pendown()
a.color("red")
a.begin_fill()
for i in range(2):
	a.forward(400)
	a.right(90)
	a.forward(260)
	a.right(90)
a.end_fill()
a.penup()
a.goto(-90,100)
a.pendown()
a.color('yellow')
a.begin_fill()
for i in range(5):
	a.forward(160)
	a.right(144)
a.end_fill()
a.penup()
a.goto(-300,300)
a.pendown()
turtle.done()