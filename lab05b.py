
# question 1
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def print_infor(self):
        print(f'Vehicle name: {self.name} speed: {self.max_speed} Mileage: {self.mileage}')


car =  Vehicle('school',240,18)
print(car.max_speed,end=' ')
print(car.mileage)
# question 2
class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage,capacity= 50):
        super().__init__(name,max_speed,mileage)
        self.capacity = capacity
    def print_infor(self):
       print(f'The seating capacity of {self.name} is {self.capacity}')

bus = Bus('school',180,12)
bus.print_infor()


class Vehicle_2:

    def __init__(self,name,max_speed,mileage,color = 'white'):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle_2):
    def __init__(self,name,max_speed,mileage,color = 'white'):
        super().__init__(name,max_speed,mileage,color = 'white')
    def print_infor_bus(self):
        print(f'{self.color} {self.name} speeed {self.max_speed} Mileage {self.mileage} ')
class Car(Vehicle_2):
    def __init__(self,name,max_speed,mileage,color = 'white'):
        super().__init__(name,max_speed,mileage,color = 'white')
    def print_infor_car(self):
        print(f'{self.color} {self.name} speeed {self.max_speed} Mileage {self.mileage} ')

car = Car('audi',180,12)
bus = Bus('School Volvo',240,18)
print(bus.print_infor_bus())
print(car.print_infor_car())

def check(objected):
    return type(objected)
print(check(car))
def check_class(object):
    if check(object) == check(car):
        return True
    return False
print(check_class(car))