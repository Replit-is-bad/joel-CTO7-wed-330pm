# import random
# import time
# list101=[]
# name='TEST'
# gender='TEST'


# while name != 'end':
#     name=input('What is your name? ')
#     gender=input('what is your gender? ')

#     num=random.randint(1,9999)
#     while num in list101:
#         num=random.randint(1,9999)

#     if num <= 9:    
#         print('your number is : '+' 000'+str(num))
#     elif num <= 99:
#         print('your number is : '+' 00'+str(num))
#     elif num <= 999:
#         print('your number is : '+' 0'+str(num))
#     else:
#         print('your number is : '+ str(num))

    
#     dude= [name,gender,num] 
#     list101.append(dude)
# print(list101)
# print('the winner is : ')
# time.sleep(2)
# name,gender



# for i in list101:
#     print(i)
    
# print('the highest num is : ' + str(max(list101)))
# print('the smallest num is : ' + str(min(list101)))
# print('the the average is : ' + str(sum(list101) / len(list101)))
# nass = random.choice(list101)
# rnass= list101.index(nass)
# print('the index is : ' + str(rnass))
# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
# for thing in contacts:
#     for item in thing:
#         print(item)

# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# boy=[]
# girl=[]
# for student in students:
#     name,gender,*sup= student
#     if gender =='M':
#         boy.append(student)
#     else:
#         girl.append(student)
# for i in boy:
#     print(i)
# for i in girl:
#     print(i)
# print('the total is: ' + str(len(students)))

