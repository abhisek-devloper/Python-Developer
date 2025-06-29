#Write a program to accept marks of 6 students and display them in a sorted manner.

print("Enter marks of 6 students:")

marks = [] # empty list

for i in range(6):
    mark = int(input())
    marks.append(mark) # add mark to the list
print("The marks are:",marks)
marks.sort() # sort the list
print("The sorted marks are:",marks)