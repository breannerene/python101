# print("hello world")
# print("My name is Bre")

# # ctrl+/ is how we make a comment 
# # this is a string example
# learner = "Bre"
# print(learner)

# # this is a number/interger example
# ideal_number_of_pets = 2
# print(ideal_number_of_pets)

# # this is a float example
# how_much_is_a_banana = 9.99
# print(how_much_is_a_banana)

# #this is a boolean example ture/false
# is_our_pets_vaccinated = True
# print(is_our_pets_vaccinated)

# print(type(learner))
# print(type(ideal_number_of_pets))
# print(type(how_much_is_a_banana))
# print(type(is_our_pets_vaccinated))

# is_it_a_number = 333
# is_this_a_number = "333"

# print(type(is_it_a_number))
# print(type(is_this_a_number))

# statement = "the number of pets I want is 2 dogs"

# puppy_name = "Buddy"
# what_is_buddys_age = 3
# how_old_is_Colton = 21.5
# is_line_26_true = True
# zipcode = "100001"

# print(statement)
# print(statement)
# print(statement)
# print(statement)

# print(5+3)
# print(5-3)
# print(5*3)
# print (5/3)
# print(10/5)
# print(7/3)
# print(12/4)
# print(99/8)

# # example of modulus operator
# print(10%3)
# print(10/3)
# print(10%5)

# # show an example of exponent operator "power to the 5th"
# print(2**5)
# print(2**2)
# print(32**73)

# # find the area of a rectangle
# length = 20
# width = 20

# area = length * width

# print(area)

# # find the tax amount
# price = 10
# tax = price * 0.08

# print(tax)

# # ask the user their favorite color
# fav_color = input("What is your favorite color? ")

# # print the favorite color
# print(f"Your favorite color is {fav_color}")

# this is a comment to test multiple inputs
# print("this", "is", "a", "test", "of", "multiple", "inputs")

# print(12, 24, -2, sep= ':')
# print('but', 'not', 'including')


# create a receipt
customer_name = input("What is your name? ")
item_price = float(input("What is the price of the item you bought? "))
quantity = int(input("How many of that item did you buy? "))
total_price = item_price * quantity
rounded_total_price = round(total_price, 2)

print("Receipt")
print("------------")
# customer Name
print(f"Customer Name: {customer_name}")
# the price of what they bought
print(f"Item Price: ${item_price}")
# the quantity of what they bought
print(f"Quantity: {quantity}")
# the total price of what they bought
print(f"Total Price: ${rounded_total_price}")
