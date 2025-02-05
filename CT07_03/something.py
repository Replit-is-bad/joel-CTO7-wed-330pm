import random
# save =int(input('how much do you have?'))

# while save < 100:
#     savings =int(input('how much have you saved today?'))
#     save += savings
# print(f'yay you have saved ${save}')




life= 3
for i in range(15):
    num1=random.randint(2,20)
    num2=random.randint(2,20)

    while life > 0:
        ans =int(input(f"what is {num1} x {num2} ? "))

        if ans == num1*num2:
            print("yes")
            break
        else:
            life -= 1
            print(f"no...now your life is {life}")
            if life == 0:
                print("GO SEE MRS TAN FOR REMEDIAL!!!")
            
            
