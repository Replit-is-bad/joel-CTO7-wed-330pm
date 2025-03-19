import time

egg = input('Give me a word or phrase: ')
isCorrect = False
egg = egg.lower()
egg = egg.split()

for word in egg:
    if 'egg' in egg:
        isCorrect = True
if isCorrect == True:
    print('Correct')
else:
    print('Worng')