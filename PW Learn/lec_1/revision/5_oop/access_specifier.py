class car:
    def __init__(self):
        self.__speed = 0                  #private member '__speed' double under score
        self._gear = 0                    #protected member '_gear' single under score
        self.carname = "Toyota"           #public member 'Toyota' no under score
    def speed_increase(self):
        self.__speed += 10
    def get_speed(self):
        print(self.__speed)

if __name__ == "__main__":
    obj = car()
    obj.speed_increase()
    obj.speed_increase()
    obj.get_speed() 
