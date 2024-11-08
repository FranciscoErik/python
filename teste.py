import turtle
t = turtle.Turtle()
t.pensize(4)
t.shape("turtle")
turtle.bgcolor("blue")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
t.color("Chocolate")
go(300, -250)
t.write("Eu te amo, minha princesa", True, "right", \
        ("Times New Roman", 40, "bold"))

t.hideturtle()
turtle.done()