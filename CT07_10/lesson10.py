import turtle



window = turtle.Screen()
window.setup(width=600 ,height=500)

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
t.speed(10)
t.seth(0)

count = 3
math = 360/count

while True: 
    for i in range (count):
        t.forward(100)
        t.left(math)
    count += 1
    math = 360/count


