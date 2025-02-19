import random
list101=[

]
for counter in range(100):
    num=random.randint(1,100)
    while num in list101:
        num=random.randint(1,100)
    list101.append(num)
for i in list101:
    print(i)
    

