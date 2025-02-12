import random
# food =[
#     'ham',
#     'burg',
#     'er',
#     'bread',
#     'candy'
# ]
# food.pop(2)
# food.append('more candy')
# for i in food:
#     print(i)

numm =[

]
while len(numm) <= 100:
    num2=(int(random.randint(1,1000)))
    while num2 in numm:
        num2=(int(random.randint(1,1000)))
    numm.append(num2)

for i in numm:
    print(i)

maxi=max(numm)
minn=min(numm)
print(maxi)
print()


