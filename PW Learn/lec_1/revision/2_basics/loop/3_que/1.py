# Write a program to print multiplication table of a given number using for loop

number = int(input("Enter a number: \n"))

print(f"{number} Multiplication Table: \n")
i = 1
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")
