import time
# print("Hello from lesson 3")

# while True:

#     ans=input(' I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? ')
#     if ans == 'idk':
#         print('you got it correct!')
#         break
#     else:
#         print('hahahahhaha')

duration = int(input('how long(in min) do you want to study for? '))
mode=input('would you like to count down or up?')
print('do you want to count in sec or in years')
if mode =='up':
    for i in range (duration,0,-1):
        print(f'you have {i} seconds remaining')
    time.sleep(1)
elif mode =='down':
    counter = 1
    while True:
        print(str(f'{counter} seconds past'))
        time.sleep(1)
        counter += 1
elif mode == 'yearly':
    print('1warning!')
    time.sleep(31536000)

else:
    print('try again')
    

