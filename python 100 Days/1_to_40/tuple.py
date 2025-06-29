#syntax example
# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)

#-------------------------------------

# country = ("Spain", "Italy", "India", "England", "Germany")
# #            [0]      [1]      [2]       [3]        [4]
# print(country[-1]) # Similar to print(country[len(country) - 1])
# print(country[-3])
# print(country[-4])
# print(len(country))

# if "spain" in country:
#     print("available")
# elif "italy" in country:
#     print("italy available")
# else:
#     print("not available")

#-------------------------------------

# animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
# print(animals[::2])     #using positive indexes
# print(animals[-8:-1:2]) #using negative indexes

#-------------------------------------

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)                       # STOP FROM 25 VDO