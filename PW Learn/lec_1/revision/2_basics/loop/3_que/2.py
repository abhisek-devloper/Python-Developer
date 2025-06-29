# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for item in l:
    
    check = str(item)
    if(check.startswith("S")):
        print(item)