# 1. Write a program to find the greatest of four numbers entered by the user.


numbers = []

for i in range(4):
    number = int(input())
    numbers.append(number)

great = 0
for i in range(4):

    if(great< numbers[i]):
        great = int(numbers[i])
        
print(great)