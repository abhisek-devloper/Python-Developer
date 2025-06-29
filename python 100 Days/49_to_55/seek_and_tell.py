# with open('myfile.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(7)

#   # Read the next 5 bytes
#   data = f.read(6)
#   print(data)
#-------------------------------------------------
# with open('myfile.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)
#   # print(data)
#   # Save the current position
#   current_position = f.tell()
#   # print(current_position)
#   # Seek to the saved position
#   f.seek(current_position)


with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  # f.truncate(5)    #remove text after 5 word only print (Hello)

with open('sample.txt', 'r') as f:
  print(f.read())