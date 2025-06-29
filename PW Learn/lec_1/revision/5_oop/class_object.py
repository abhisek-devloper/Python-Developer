class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def info(self):
        print(self.brand, self.model)

if __name__ == "__main__":
    brand = str(input())
    model = str(input())
    
    car_obj = Car(brand,model)
    car_obj.info()
