#################################################################
# Question 1
# A e-commerce store keeps track of their sales figures each day 
# for the month of August. 
# The sales for the 31 days are provided in the list below. 

# Write Code to:
# a) Find the day with the highest sales 
# b) Find the day with the lowest sales
# c) Find the average daily sales for August (to 2 decimal place)
    

# Example Output/ Answer:
# 5 August has highest sales of $15741
# 7 August has lowest sales of $800
# Average daily sales for August is $6714.71


# Assume that first item in list is 1 August (not zero!)
# You are allowed to use the inbuilt functions e.g. max()
##########################################################
daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
               13056, 952, 1100, 1025, 8574, 14014, 9987, 
               1238, 1458, 7803, 900, 13674, 14539, 13241, 
               10886, 7541, 8743, 1482, 11523, 977, 12181, 
               8903, 1008, 1530]
# Write your code here.
numcc =0
numc = 0

#highest number
highests = max(daily_sales)

#lowest number
lowests = min(daily_sales)

#amount of item in list
count = len(daily_sales)

#sum of all items
totalnum = sum(daily_sales)

#average
avge = round(totalnum / count,2)

for i in daily_sales:
    numc += 1
    if i == highests:
        counth = numc

for i in daily_sales:
    numcc += 1
    if i == lowests:
        countL = numcc

print(f'{counth} August has highest sales of ${highests}')
print(f'{countL} August has lowest sales of ${lowests}')
print(f'Average daliy sales for August is ${avge}')











##########################################################