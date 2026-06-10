#constuctor
class Student():
    def __init__(self,name,age):
        print("Student obj is created...!")
        self.name=name
        self.age=age
def details(self):
    print("----------------")
    print(f"name is {self.name}")
    print(f"age is {self.age}")
s1=Student('scott',23)
details(s1)
s2=Student('allen',24)
details(s2)

#product.py
class Product:
    def __init__(self,name,price):
        print("Product object is created.....!")
        self.name=name
        self.price=price
        print("-------------")
P1=Product('phone',2000)
print(f"name={P1.name}")
print(f"price={P1.price}")
P2=Product('laptop',50000)
print(f"name={P2.name}")
print(f"price={P2.price}")
P3=Product('macbook',55000)
print(f"name={P3.name}")
print(f"price={P3.price}")

#ass 1
class Mobile:
    def __init__(self,brand,price,color):
        print("Product object is created.....!") 
        self.brand=brand 
        self.price=price
        self.color=color
        print("--------")
P1=Mobile('redmi',15000,'black')
print(f"brand={P1.brand}")
print(f"price={P1.price}")
print(f"color={P1.color}")
P2=Mobile('realmi',20000,'red')
print(f"brand={P2.brand}")
print(f"price={P2.price}")
print(f"color={P2.color}")

#ass 2
class Employee:
    def __init__(self,name,id,sal,dept):
        print("Product object is created.....!") 
        self.name=name 
        self.id=id
        self.sal=sal
        self.dept=dept
        print("--------")
E1=Employee('radha',1,15000,'hr')
print(f"name={E1.name}")
print(f"id={E1.id}")
print(f"sal={E1.sal}")
print(f"dept={E1.dept}")

