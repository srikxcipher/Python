import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Easy level
# passw = ""
#
# range(1, )
#
# for char in range(0, nr_letters):
#     passw += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     passw += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     passw += random.choice(numbers)
#
# print(passw)

# Hard level
passw_list = []

range(1, )

for char in range(0, nr_letters):
    passw_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    passw_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    passw_list.append(random.choice(numbers))

print(passw_list)

random.shuffle(passw_list)

print(passw_list)

password = ""

for char in passw_list:
    password += char

print(f"Your password is: '{password}'")

print("Length of the password is ,", len(password))



