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


window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('gold3')

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
t.penc
window.mainloop()
