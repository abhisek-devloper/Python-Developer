# Write a program to calculate the factorial of a given number using for loop.

number = int(input("Enter a number:"))

i = number
factorial = 1
while(i>0):
    factorial *= i
    i = i - 1
print(factorial)