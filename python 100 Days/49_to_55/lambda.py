# # Function to double the input
# def double(x):
#   return x * 2

# # Lambda function to double the input
# lambda x: x * 2

# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

print(multiply(5,2))

# Lambda function to calculate the product of two numbers
multi = lambda x, y: x * y
print(multi(4,3))


multiply_lambda = lambda x, y: print(f'{x} * {y} = {x * y}') #declare

multiply_lambda(5, 2) #call
