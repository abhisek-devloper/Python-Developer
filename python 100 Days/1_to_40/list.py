# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)
#---------------------------------------------------
# colors = ["voilet", "indigo", "blue", "green"]
# colors.sort(reverse=True) # for descending
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort(reverse=True) # for descending
# print(num)
#---------------------------------------------------
# colors = ["voilet", "indigo", "blue"]
# #           [0]        [1]      [2]

# colors.insert(1, "green")   #inserts item at index 1
# # updated list: colors = ["voilet", "green", "indigo", "blue"]
# #       indexs              [0]       [1]       [2]      [3]

# print(colors)
#---------------------------------------------------
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)