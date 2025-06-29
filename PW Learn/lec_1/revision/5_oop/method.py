class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 *self.radius*self.radius
        
if __name__ == "__main__":
    circle_instance = circle(5)
    
print(circle_instance.area())
