#Write a program to store seven fruits in a list entered by the user.

print("Enter seven fruits:")

fruits = [] # empty list

for i in range(7):
    fruit = input()
    fruits.append(fruit) # add fruit to the list
print("The fruits are:",fruits)
    