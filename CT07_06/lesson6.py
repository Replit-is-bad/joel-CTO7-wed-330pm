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
    
print('the highest num is : ' + str(max(list101)))
print('the smallest num is : ' + str(min(list101)))
print('the the average is : ' + str(sum(list101) (len(list101))))
