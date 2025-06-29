# def add(a = 10, b=20):
#     x = a+b
#     return x

# print(add(b=5,a=3))

def average(*numbers):   #accept list
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/ len(numbers))


average(5,6,7)

def student_list(**numbers):   #accept dictionary
    
    for i in numbers:
        print( i , " = ", numbers[i]) # print only key

student_list(name = "abhisek", age = 18)

