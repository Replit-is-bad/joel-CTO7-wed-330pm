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
window.setup(width=700, height=500)
window.bgcolor('gold3')

t = turtle.Turtle()
t.shape("square")
t.fillcolor("forestgreen")
t.speed(10)

t.stamp()
t.sety(250)
for i in range (25):
    t.stamp()
    
window.mainloop()
