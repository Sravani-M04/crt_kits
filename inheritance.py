#sigle inheritance
class Vehicle:
    def __init__(self,b,p,c,s):
        self.b=b
        self.p=p
        self.c=c
        self.s=s
        print('Vehicle class Constructor')
class Bike(Vehicle):
    def __init__(self,b,p,c,s,g,m):
        super().__init__(b,p,c,s)
        self.g=g
        self.m=m
        print('Bike class constructor')
b1=Bike('Tata',25000,'black',2,3,45)

#multilevel
class Vehicle:
    def __init__(self, b, p, c, s):
        self.b = b
        self.p = p
        self.c = c
        self.s = s
        print('Vehicle class Constructor')

class Bike(Vehicle):
    def __init__(self, b, p, c, s, g, m):
        super().__init__(b, p, c, s)
        self.g = g
        self.m = m
        print('Bike class constructor')

class SportsBike(Bike):
    def __init__(self, b, p, c, s, g, m, top_speed):
        super().__init__(b, p, c, s, g, m)
        self.top_speed = top_speed
        print('SportsBike class constructor')

b1 = SportsBike('Tata', 25000, 'black', 2, 3, 45, 180)

#hierarchical
class Vehicle:
    def __init__(self, b, p, c, s):
        self.b = b
        self.p = p
        self.c = c
        self.s = s
        print('Vehicle class Constructor')

class Bike(Vehicle):  # Level 1
    def __init__(self, b, p, c, s, g, m):
        super().__init__(b, p, c, s)
        self.g = g
        self.m = m
        print('Bike class constructor')

class SportsBike(Bike):  # Multilevel: Vehicle → Bike → SportsBike
    def __init__(self, b, p, c, s, g, m, top_speed):
        super().__init__(b, p, c, s, g, m)
        self.top_speed = top_speed
        print('SportsBike class constructor')

class Car(Vehicle):  # Hierarchical: Vehicle → Car
    def __init__(self, b, p, c, s, doors):
        super().__init__(b, p, c, s)
        self.doors = doors
        print('Car class constructor')

b1 = SportsBike('Tata', 25000, 'black', 2, 3, 45, 180)
c1 = Car('Maruti', 500000, 'white', 4, 4)

#multiple 
class Vehicle:
    def __init__(self, b, p, c, s):
        self.b = b
        self.p = p
        self.c = c
        self.s = s
        print('Vehicle class Constructor')

class ElectricFeatures:
    def __init__(self, battery, range_km):
        self.battery = battery
        self.range_km = range_km
        print('ElectricFeatures class Constructor')

class Bike(Vehicle):  # Hierarchical: Vehicle → Bike
    def __init__(self, b, p, c, s, g, m):
        super().__init__(b, p, c, s)
        self.g = g
        self.m = m
        print('Bike class constructor')

class Car(Vehicle):  # Hierarchical: Vehicle → Car
    def __init__(self, b, p, c, s, doors):
        super().__init__(b, p, c, s)
        self.doors = doors
        print('Car class constructor')

class SportsBike(Bike, ElectricFeatures):  # Multiple + Multilevel
    def __init__(self, b, p, c, s, g, m, battery, range_km, top_speed):
        Bike.__init__(self, b, p, c, s, g, m)  # for Vehicle part
        ElectricFeatures.__init__(self, battery, range_km)  # for Electric part
        self.top_speed = top_speed
        print('SportsBike class constructor')

b1 = SportsBike('Tata', 25000, 'black', 2, 3, 45, 3.5, 120, 180)

#hybrid
class Vehicle:
    def __init__(self, b, p, c, s):
        self.b = b; self.p = p; self.c = c; self.s = s
        print('Vehicle Constructor')

class ElectricFeatures:
    def __init__(self, battery):
        self.battery = battery
        print('ElectricFeatures Constructor')

class Bike(Vehicle):  # Hierarchical + Multilevel base
    def __init__(self, b, p, c, s, gears):
        super().__init__(b, p, c, s)
        self.gears = gears
        print('Bike Constructor')

class Car(Vehicle):  # Hierarchical
    def __init__(self, b, p, c, s, doors):
        super().__init__(b, p, c, s)
        self.doors = doors
        print('Car Constructor')

class SportsBike(Bike, ElectricFeatures):  # Multiple + Multilevel
    def __init__(self, b, p, c, s, gears, battery, speed):
        Bike.__init__(self, b, p, c, s, gears)
        ElectricFeatures.__init__(self, battery)
        self.speed = speed
        print('SportsBike Constructor')

class ElectricSportsBike(SportsBike):  # Multilevel on top of hybrid
    def __init__(self, b, p, c, s, gears, battery, speed, turbo):
        super().__init__(b, p, c, s, gears, battery, speed)
        self.turbo = turbo
        print('ElectricSportsBike Constructor')

e1 = ElectricSportsBike('Yamaha', 150000, 'blue', 2, 6, 5.2, 220, True)
        
