#polymorphism
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak tabdak ")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)

# overriding
class Engineer:
    def __init__(self):
        pass
    def work(self):
        print("Engineer is working...!")
class SoftwareEngineer(Engineer):
    def __init__(self):
        super().__init__()
    def work(self):
        print("Software engineer is working")
e1=Engineer()
e1.work()
s1=SoftwareEngineer()
s1.work()

#Encapsulation
class BankAccount:
    def __init__(self,name,acc_no,pin):
        self.__name=name
        self.__acc_no=acc_no
        self.__pin=pin
        print('BAnk account is created')
    def get_name(self):
        print(self.__name)
    def get_accno(self):
        print(self.__acc_no)
    def get_pin(self):
        print(self.__pin)
b1=BankAccount('scott',1234567890,1234)
b1.get_name()
b1.get_accno()
b1.get_pin()
