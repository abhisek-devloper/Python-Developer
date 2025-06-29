class cat:
    def make_sound(self):
        return "Meow"
class dog:
    def make_sound(self):
        return "woof"

def animal_sound(animal):
    print(animal.make_sound())

if __name__ == "__main__":
    #create a object
    cat = cat()  
    dog = dog()
    
    #function call with object parameter
    animal_sound(dog) 
    animal_sound(cat)
    
