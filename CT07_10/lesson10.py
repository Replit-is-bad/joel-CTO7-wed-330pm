import turtle



window = turtle.Screen()
window.setup(width=500 ,height=500)

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
t.speed(10)
t.seth(0)

count = 3
math = 360/count

for i in range (5):
    t.forward(100)
    t.left(72)

window.mainloop()