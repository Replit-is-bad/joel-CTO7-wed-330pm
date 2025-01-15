import random



# count = 2
# while count <= 24:
#     print(count)
#     count = count + 1

# count = 1
# while count <= 30:
#     print(count)
#     count = count + 1

# count = 0
# while count <= 20:
#     print(count)
#     count = count + 1
#     #count += 1

# count=0
# while True:
#     if count == 20:
#         break
#     print(count)
#     count+=1

# validation/question\
num1=random.randint(1,10)
num2=random.randint(1,10)
life= 9
while True:
    ans =int(input(f"what is {num1} + {num2}?"))

    if ans == num1+num2:
        print("yes")
        break
    else:
        if life == 0:
            print("YOU DIED")
        life -= 1
        print(f"no...now your life is {life}")
        
