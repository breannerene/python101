
# If statements
# An if statement is used to compare things

# variable = input("This is an input that will take a response")
# print(variable)

#going to ride the coney isalnd rollercoaster
# 4' aka 48"
# height = int(input("How tall are you? "))
# #height >=48
# if height >= 48:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you are not tall enough to ride the rollercoaster.")

# create a password checker
# username = HotDogWater123
# password = bluepen

# password = "bluepen" 

# userLoginInput = input("Enter Password: ")




# check if number is even or odd using the != (not equal to operator):
# number = int(input("Enter a number: "))

# if number % 2 != 0:
#     print("odd")
# else:
#     print("even")    


# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")    


# # print(5/2)
# # print(4/2)
# print(11%3)
# print(11%5)
# print(11%7)
# print(11%2)

# Write a forLoop for the value 1-1152
# numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for number in range (1, 153):
#     print(number)

# coutndown from 10 -0
# for number in range(10, 0, -1):
#     print(number)
#     #print statement is inside forLoop, so it will print each time
#     #print("Blast off!")
# print("Blast off!")

#Who likes root beer?
# numberofRootBeers = 31

# for i in range(numberofRootBeers, 1, -1):
#     print(f"{i} bottles of root beer on the wall...")
#     print(f"{i} bottles of root beer")
#     print("take on down, pass it around...")
#     print(f"{i-1} bottles of root beer on the wall!")

# Wahat is the sum of 1-427
# total = 0

# for number in range(1, 428):
#     total += number

# print(f"Your total is: {total}")

# #what is the sum of 1-427
# # total = int(input("Pick a number to add up to: " ))

# # for number in range(1, total+1):

# # find the largest number
from ast import While


numberList = [7, 42, 8, 946, -1, 4235, 6, 730]

# first number in this case is 7
# largestNumber = numberList[0]

# for number in numberList:
#     # first interaction says "is 7 larger than 7? if not move on to the second iteration,
#     # if so, then the new largest number becomes the value we're checking in the list"
#     if number > largestNumber:
#         largestNumber = number

# print(largestNumber)

# Who wants to play... GUESS THAT NUMBER!
secretNumber = 7

guess = 0
while guess != secretNumber:
    guess = int(input("Guess the secret number: "))

print("You got it!")