# students=[]
# student1=['name','999','toilet inspetor']
# student2=['name','939','toilet inspetor']
# student3=['name','993','toilet inspetor']

# students.append(student1)
# students.append(student2)
# students.append(student3)

# for thing in students:
#     name, number, cca = thing
#     print("Name: " + name)
#     print("Number: " + str(number))
#     print("CCA: " + cca)


# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# fruits= list1+list2

# stor=sorted(fruits)
# print(stor)

# index = len(fruits)//2

# print(fruits[:index])
# print(fruits[index:])

# common=[]
# uncommon=[]
# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# for thing in list1:
#     if thing in list2:
#         common.append(thing)
#     else:
#         uncommon.append(thing)

# for thing in list2:
#     if thing in list1:
#         common.append(thing)
#     else:
#         uncommon.append(thing)

# print(uncommon)



# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# even =[]
# student=list1+list2
# for dud in student:
#     if dud % 2 == 0:
#         even.append(dud)

# print(even)
new=[]
students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3

for i in range(0,len(students),size):
    new.append(students[i:i+size])

print(new)
