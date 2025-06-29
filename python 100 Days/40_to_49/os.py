import os

# os.mkdir("hello") # create directory

#create multiple directory
# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/data{i+1}")

#--------------------------------------
# # Open the file in write-only mode
# f = os.open("myfile.txt", os.O_WRONLY)

# # Write to the file
# os.write(f, b"Hello, world!")

# # Open the file in read-only mode
# f = os.open("myfile.txt", os.O_RDONLY)

# # Read the contents of the file
# contents = os.read(f, 1024)

# # Close the file
# os.close(f) 

#-----------------------------------------

files = os.listdir(".")
print(files) 
