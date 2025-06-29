class Student:
    def __init__(self, name, age):
        self._name = name  # Private attribute (convention: underscore prefix)
        self._age = age

    # Getter method for name
    @property
    def name(self):
        return self._name

    # Setter method for name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():  # Validation
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string!")

    # Getter method for age
    @property
    def age(self):
        return self._age

    # Setter method for age
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:  # Validation
            self._age = new_age
        else:
            raise ValueError("Age must be a positive integer!")

# Creating an object
student = Student("Alice", 21)

# Using getter
print(student.name)  # Output: Alice
print(student.age)   # Output: 21

# Using setter
student.name = "Bob"
student.age = 25

print(student.name)  # Output: Bob
print(student.age)   # Output: 25

# Trying to set an invalid name
# student.name = ""  # Raises ValueError: Name must be a non-empty string!
