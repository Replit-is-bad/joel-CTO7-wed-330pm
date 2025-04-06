import random
import time



herohp = 100
counter = 0

Monster = [
    'hi'
]

print('Hero starts on his adventure with Health: ' + str(herohp))
time.sleep(0.5)
while herohp >= 0:
    dmg = random.randint(1,15)
    herohp -= dmg
    if herohp <= 0:
        break
    else:
        print('After fighting monsters, his Health is now: ' + str(herohp))
        counter += 1
        time.sleep(1)
print('Your hero died fighting ' + str(counter) + ' monsters')



# strr = 'A,B,C,D,E,F'
# list = strr.split(',')

# print(list)



# cust = input('What would u like to order? ')
# order =[]

# while cust != 'end':
#     order.append(cust)
#     cust = input('What would u like to order? ')

# print('U have ordered the following: ')
# count=1
# for i in order:
#     print(str(count) +'. ' +i)
#     count += 1
    