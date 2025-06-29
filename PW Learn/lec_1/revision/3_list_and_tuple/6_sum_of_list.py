#Write a program to sum a list with 4 numbers.

l1 = [1,2,4,5]

sum = 0
for i in range(len(l1)):
    sum = sum + l1[i]
    print(sum)

# or

# for i in l1:
#     sum = sum + i

# print(sum)