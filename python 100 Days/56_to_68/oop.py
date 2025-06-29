# #create class and object
# class Details:
#     name = "abhisek"
#     age = 20

# obj1 = Details()
# print(obj1.name,obj1.age)

class Details:
    name = "Rohan"
    age = 20

    def desc(self): # self is this object
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()


