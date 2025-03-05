import random


herohp = 100
counter = 0

print('Hero starts on his adventure with Health: ' + str(herohp))
while herohp >= 0:
    dmg = random.randint(1,15)
    herohp -= dmg
    if herohp <= 0:
        break
    else:
        print('After fighting monsters, his Health is now: ' + str(herohp))
        counter += 1
print('Your hero died fighting ' + str(counter) + ' monsters')



# strr = 'A,B,C,D,E,F'
# list = strr.split(',')

# print(list)