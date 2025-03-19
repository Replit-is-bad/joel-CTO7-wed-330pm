'''
list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
list4 =[]
dup =[]
uni =[]

list4 = list1 + list2 +list3

for num in list4:
    if num not in uni:
       uni.append(num)
uni = sorted(uni)
print(uni)

mid = len(uni) //2
print(mid)


meme = input("say something: ")
counter = 0
end =''

for counter in range (len(meme)):
    if counter % 2 ==0:
        end = end + meme[counter].upper()
    else:
        end = end + meme[counter].lower()
print(end)
'''



strr = "Computers empower our modern world with their digital brains."
list = strr.split(' ')
print(list)

string = ' '.join(list)
print(string)