import random
import turtle

# egg = input('Give me a word or phrase: ')
# isCorrect = False
# egg = egg.lower()
# egg = egg.split()


# if 'egg' in egg:
#     print('Correct')
# else:
#     print('Worng')
guess = input('Guess the winner: ')
Winner = ''

window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('grey')

t = turtle.Turtle()
t.shape("square")
t.fillcolor("forestgreen")
t.speed(10)

t.up()
t.sety(250)
for i in range(-300,301,25):
    t.setx(i)
    t.stamp()

t.goto(-300,-250)
t.seth(0)
t.pencolor('yellow')
t.down()
t.forward(600)
t.hideturtle

#player : Bullpoop
Sally =turtle.Turtle()
Sally.penup()
Sally.seth(90)
Sally.shape('turtle')
Sally.color('red')
Sally.goto(0,-250)
Sally.write('Sally', align='center', font=('Arial', 20))

#player : Bullpoop
Bullpoop =turtle.Turtle()
Bullpoop.penup()
Bullpoop.seth(90)
Bullpoop.shape('turtle')
Bullpoop.color('azure')
Bullpoop.goto(200,-250)
Bullpoop.write('Bullpoop', align='center', font=('Arial', 20))

#player : sigma
sigma =turtle.Turtle()
sigma.penup()
sigma.seth(90)
sigma.shape('turtle')
sigma.color('blue')
sigma.goto(-200,-250)
sigma.write('sigma', align='center', font=('Arial', 20))

sigma.down()
Sally.down()
Bullpoop.down()
while True:
    Sally.seth(random.randint(75,115))
    Bullpoop.seth(random.randint(75,115))
    sigma.seth(random.randint(75,115))

    Sally.forward(random.randint(1,20))
    Bullpoop.forward(random.randint(1,20))
    sigma.forward(random.randint(1,20))

    if Sally.ycor() > 250:
        winner
window.mainloop()

