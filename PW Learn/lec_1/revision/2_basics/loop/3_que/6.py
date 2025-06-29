# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3


n = 3
for i in range(n):
    spaces = ' ' * (n - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
