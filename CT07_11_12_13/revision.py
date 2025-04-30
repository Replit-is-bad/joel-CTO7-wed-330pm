
# Write a program to find the largest and smallest numbers in 
# a list using 
# 1a. max()
# 1b. min()
# 1c. without using max()
# 1d. without using min()
# 1e. find the sum of all the numbers
# 1f. find the count of items in the list
# 1g. find the average of all the numbers
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

####################################################
# Answer for Question 1a here
maxnum = max(list1)
print(f"The biggest number is {maxnum}")

####################################################
# Answer for Question 1b here
minnum = min(list1)
print(f"The smallest number is {minnum}")

####################################################
# Answer for Question 1c here
maxnum2 = 0
for num in list1:
    if num > maxnum2:
        maxnum2 = num
print(f"The biggest number is {maxnum2}")

####################################################
# Answer for Question 1d here
minnum2 = 9999
for i in list1:
    if i < minnum2:
        minnum2 = i
print(f"The smallest number is {minnum2}")

####################################################
# 1e. find the sum of all the numbers
sumnum = 0
for i in list1:
    sumnum += i
print(f"The sum of all numbers is {sumnum}")
####################################################
# 1f. find the count of items in the list
countnum = 0
for i in list1:
    countnum += 1
print(f"The amount of numbers is {countnum}")

####################################################
# 1g. find the average of all the numbers
avrnum = sumnum / countnum
print(f"The average is {avrnum}")

######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# Answer for Question 2 here

fastlane = 0
slowlane = 0
slowest = 40
count = 0
counts = 0

for i in swim_times:
    if i < slowest:
        slowest = i
        slowlane = count
    count += 1
print(f"The slowest time is {slowest}")
print(f"his lane num is {slowlane}")

fastest = 0
for i in swim_times:
    if i > fastest:
        fastest = i
        fastlane = counts
    counts += 1
print(f"The fastest time is {fastest}")
print(f"The fastest lane num is {fastlane}")








#################################################################
# Question 4: 
# A bookstore keeps track of their sales figures each day 
# for the month of June. The sales for the 30 days are provided 
# in the list below. Find the days with the highest and lowest sales. 
# Assume that the first item in the list corresponds to Day 1.

# Find the total sales figure for the month
# Find the average sales rounded to 2 decimal points
#################################################################
daily_sales = [120, 98, 135, 105, 150, 112, 80, 130, 95, 110, 
               102, 85, 140, 99, 123, 145, 78, 90, 136, 145, 
               132, 108, 75, 88, 142, 115, 97, 121, 89, 100]
# Answer for Question 4 here
count = 0
days = 0
lowest = 200
for i in daily_sales:
    if i < lowest:
        lowest = i
        days = count
    count += 1
print(f"the lowest sales are {lowest} on the {days} of June")

count = 0
days = 0
most = 0
for i in daily_sales:
    if i > most:
        most = i
        days = count
    count += 1
print(f"the highest sales is {most} on the {days} of June")



##################################################################
# Question 5: 
# Hourly temperature measurements (°C) for a specific day are given below. 
# Write Python code to determine the highest and lowest temperatures, 
# along with the corresponding hour of measurement. 
# (First measurement at index 0 corresponds to midnight, 
#  and each subsequent value is measured hourly.)

# Find the average temperature for this day.
##################################################################
hourly_temperatures = [26.4, 25.9, 25.1, 24.6, 24.2, 23.8, 24.5, 25.6, 
                       27.3, 29.0, 30.5, 31.2, 32.0, 33.1, 32.8, 31.6,
                       30.8, 29.4, 28.1, 27.5, 27.0, 26.8, 26.0, 25.7]
# Answer for Question 5 here
count = 0
days = 0
lowest = 100
for i in hourly_temperatures:
    if i < lowest:
        lowest = i
        days = count
    count += 1
print(f"the lowest temp are {lowest} on the hour {days} of June")

count = 0
days = 0
most = 0
for i in hourly_temperatures:
    if i > most:
        most = i
        days = count
    count += 1
print(f"the highest temp is {most} on the hour {days} ")

sumnum = 0
for i in hourly_temperatures:
    sumnum += i
print(f"The sum of all numbers is {sumnum}")

average = sumnum / 24
print(f"The average of the day is {round(average,2)}")


word = 'hi'

if word == word[::-1]:
    print('gi')


suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']
