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



# validation/question
# life= 10
# for i in range(10):
#     num1=random.randint(1,10)
#     num2=random.randint(1,10)

#     while life > 0:
#         ans =int(input(f"what is {num1} + {num2}?"))

#         if ans == num1+num2:
#             print("yes")
#             break
#         else:
#             life -= 1
#             print(f"no...now your life is {life}")
#             if life == 0:
#                 print("YOU DIED")
#                 break
            
#     else:
#         continue


#
topping=''
cost=15.50
print('welcome to tuh azzip ')
while True :
    top = input("What toppings do you want?type 'end' to stop: ")
    
    if top == 'end':
        print("Thank you")
        break
    else:
        topping = topping +top +" ,"
        cost += 3.50
print(f"your topings are: {topping}")
print(f"the cost of your azzip is :{cost}")
