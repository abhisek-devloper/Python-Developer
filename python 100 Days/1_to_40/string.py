# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

#---------------------------- Format string
# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")  
# name = 'Tushar'  
# age = 23  
# print(f"Hello, My name is {name} and I'm {age} years old.")


#---------------------- Docstrings  // write document 

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)
# square(5)

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__) # print docstring