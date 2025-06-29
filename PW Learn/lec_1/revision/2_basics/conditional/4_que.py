# 4. Write a program to find whether a given username contains less than 10 characters or not.

# Take username input from the user
username = input("Enter your username: ")

# Check the length
if len(username) < 10:
    print("✅ The username contains LESS than 10 characters.")
else:
    print("❌ The username contains 10 or MORE characters.")
