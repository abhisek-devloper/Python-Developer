# 5.Write a program which finds out whether a given name is present in a list or not.

# Predefined list of names
name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Input name from user
name = input("Enter a name to search: ")

# Check presence
if name in name_list:
    print(f"✅ {name} is present in the list.")
else:
    print(f"❌ {name} is not present in the list.")
