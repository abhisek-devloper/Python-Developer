#Write a python program to calculate the square of a number entered by the user.

num = int(input("Enter a number: "))  # By default input is a string, so we need to convert it to an integer

square = num ** 2   #  { ** is the exponentiation operator in Python }
# or square = num * num


print("The square of", num, "is:", square)