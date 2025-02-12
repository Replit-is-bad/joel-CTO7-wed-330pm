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

# numm =[

# ]
# while len(numm) <= 100:
#     num2=(random.randint(1,1000))
#     while num2 in numm:
#         num2=(random.randint(1,1000))
#     numm.append(num2)

# for i in numm:
#     print(i)

# maxi=max(numm)
# minn=min(numm)
# print('the max is : '+ str(maxi))
# print('the min is : '+ str(minn))



# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#  "Sophia", "Lucas", "Mia", "Aiden"
# ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# hig=max(heightlist)
# inthe=heightlist.index(hig)
# guyh=namelist.pop(inthe)
# print(str(hig) + guyh)


pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]
powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]
poki1=random.choice(pokemons)
pow=powers[pokemons.index (poki1)]
print(str(pow) + ' : '+ poki1)

poki2=random.choice(pokemons)
inhis2=pokemons.index(poki2)
pow2=powers.pop(inhis2)
print(str(pow2) + ' : '+ poki2)



if pow2 != pow:
    if pow > pow2:
        print(poki1 + " wins!!")
    else:
        print(poki2 + " wins!!")
else:
    print('! tie !')
    