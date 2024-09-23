from turtle import color, back, left, forward, right, pensize
import turtle

t = turtle.Turtle()

# Mengatur ukuran pensil
pensize(5)

# Mengatur warna dan menggambar pola
color("white")
back(450)
color("black")

left(90)
forward(100)
back(100)
right(90)

color("white")
forward(100)
left(90)

color("black")
forward(100)
back(100)
right(90)

color("black")
forward(50)
color("white")
forward(50)

color("black")
forward(50)
back(50)
left(90)
forward(100)
right(90)

color("white")
forward(110)
left(120)
forward(110)

# Menyelesaikan drawing
turtle.done()