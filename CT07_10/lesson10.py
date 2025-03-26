import turtle



window = turtle.Screen()
window.setup(width=500 ,height=500)

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
t.speed(10)
t.seth

for i in range (4):
    t.forward(100)
    t.left(90)

