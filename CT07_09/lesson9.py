import time

egg = input('Give me a word or phrase: ')
isCorrect = fla
egg = egg.lower()
egg = egg.split()

for word in egg:
    if egg == 'egg':
        print('correct')
        time.sleep(1)
