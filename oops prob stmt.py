# ATS
class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
    def show(self):
        print(f"Name: {self.name}, Skills: {self.skills}")
class Job:
    def __init__(self, title, required_skills):
        self.title = title
        self.required_skills = required_skills
    def check_match(self, candidate):
        match = 0
        for skill in candidate.skills:
            if skill in self.required_skills:
                match += 1
        return match
class Application:
    def __init__(self, candidate, job):
        self.candidate = candidate
        self.job = job
        self.status = "Applied"
    def show_status(self):
        print(f"{self.candidate.name} applied for {self.job.title} - Status: {self.status}")
c1 = Candidate("Riya", ["Python", "SQL", "HTML"])
c2 = Candidate("Aman", ["Java", "C++"])
c3=Candidate("priya",["java","Python","c++","SQL"])
job1 = Job("Python Developer", ["Python", "Django", "SQL"])
app1 = Application(c1, job1)
app2 = Application(c2, job1)
app3=Application(c3,job1)
app1.show_status()
print(f"Skill match score: {app1.job.check_match(c1)} / {len(job1.required_skills)}")
app2.show_status()
print(f"Skill match score: {app2.job.check_match(c2)} / {len(job1.required_skills)}")
app3.show_status()
print(f"Skill match score: {app3.job.check_match(c3)} / {len(job1.required_skills)}")

# emp working hours
class Emp:
    def work_hours(self):
        print("employee works 8 hours in a day")
class Intern(Emp):
    def work_hours(self):
        super().__init__()
        print("intern works 6 hours a day")
intern=Intern()
intern.work_hours()

# food delivery company
class Cus:
    def delivery_charge(self):
        print("Delivery Charge: 50")
class PrimeCus(Cus):
    def delivery_charge(self):
        print("Delivery Charge: 20")
print("Customer")
c1 = Cus()
c1.delivery_charge()
print("Prime Customer")
c2=PrimeCus()
c2.delivery_charge()

# multiplex offers
class Ticket:
    def price(self):
        print("Ticket Price: ₹150")
class VIPTicket(Ticket):
    def price(self):
        print("Ticket Price: ₹500")
print("VIP Ticket")
vip = VIPTicket()
vip.price()
print("Ticket")
tic=Ticket()
tic.price()

# bank offer
class Bank:
    def interest_rate(self):
        print("Interest Rate: 4%")
class PrivateBank(Bank):
    def interest_rate(self):
        print("Interest Rate: 6%")
print("Test Case 1 - Private Bank")
pb = PrivateBank()
pb.interest_rate()

# learning platform fee
class Course:
    def course_fee(self):
        print("Course Fee: ₹5000")
class AdvancedCourse(Course):
    def course_fee(self):
        print("Course Fee: ₹12000")
print("Advanced Course")
ac = AdvancedCourse()
ac.course_fee()
print("\nBasic Course")
bc = Course()
bc.course_fee()

# ride booking offer
class Ride:
    def fare(self):
        print("Fare: ₹100")
class LuxuryRide(Ride):
    def fare(self):
        print("Fare: ₹300")
print(" Luxury Ride")
l1 = LuxuryRide()
l1.fare()
print("\nNormal Ride")
r1 = Ride()
r1.fare()

# subscrition
class Subscription:
    def features(self):
        print("Watch videos with ads")
class PremiumSubscription(Subscription):
    def features(self):
        print("Watch videos without ads")
print("Premium Plan")
p1 = PremiumSubscription()
p1.features()
print("\nBasic Plan")
s1 = Subscription()
s1.features()

# vehicle
class Vehicle:
    def max_speed(self):
        print("Maximum Speed: 80 km/h")
class SportsCar(Vehicle):
    def max_speed(self):
        print("Maximum Speed: 250 km/h")
print("Test Case 1 - Sports Car")
s1 = SportsCar()
s1.max_speed()
print("\nVehicle")
v1 = Vehicle()
v1.max_speed()

# bonus
class Employee:
    def bonus(self):
        print("Bonus: ₹5000")
class Manager(Employee):
    def bonus(self):
        print("Bonus: ₹20000")
print("Manager")
m1 = Manager()
m1.bonus()
print("\nEmployee")
e1 = Employee()
e1.bonus()

# training institute eligibility
class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60")
class AdvancedStudent(Student):
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80")
print(" Advanced Student")
a1 = AdvancedStudent()
a1.placement_status()
print("\n Regular Student")
s1 = Student()
s1.placement_status()

# cafeteria
class Employee:
    def __init__(self, e_id, e_name):
        self.e_id=e_id
        self.e_name=e_name
class FoodItem:
    def __init__(self, item_name, price):
        self.item_name=item_name
        self.price=price
class Order:
    def __init__(self, ord_id):
        self.ord_id=ord_id
        self.ord_items=[]
    def add_item(self, item):
        self.ord_items.append(item)
    def calculate_total(self):
        return sum(item.price for item in self.ord_items)
    def generate_bill(self, employee):
        print("="*50)
        print("       CORPORATE CAFETERIA BILL")
        print("="*50)
        print()
        print(f"Employee ID:{employee.e_id}")
        print(f"Employee Name:{employee.e_name}")
        print()
        print("-"*50)
        print(f"{'Item':<28}Price")
        print("-"*50)
        for item in self.ord_items:
            print(f"{item.item_name:<28}rs{item.price}")
        print("-" * 50)
        print()
        print(f"{'Total Amount':<28}rs{self.calculate_total()}")
        print()
        print(f"{'Payment Status':<28}PAID")
        print()
        print("="*50)
class Cafeteria:
    def __init__(self):
        self.menu = []
    def add_food_item(self, item):
        self.menu.append(item)
    def display_menu(self):
        for item in self.menu:
            print(f"{item.item_name} {item.price}")
employee = Employee("E101", "Ryan")
cafeteria = Cafeteria()
cafeteria.add_food_item(FoodItem('Coffee', 40))
cafeteria.add_food_item(FoodItem('Sandwich', 80))
cafeteria.add_food_item(FoodItem('Brownie', 60))
ord = Order("O101")
ord.add_item(cafeteria.menu[0])  
ord.add_item(cafeteria.menu[1])  
ord.add_item(cafeteria.menu[2])  
ord.generate_bill(employee)

# multiplex ticket booking
class Customer:
    def __init__(self, name):
        self.customer_name=name
class Movie:
    def __init__(self, name, price):
        self.movie_name=name
        self.ticket_price=price
class Booking:
    def __init__(self, customer, movie, tickets):
        self.customer=customer
        self.movie=movie
        self.number_of_tickets=tickets
        self.booking_status=False
    def book_ticket(self):
        self.booking_status=True
    def calculate_amount(self):
        return self.movie.ticket_price*self.number_of_tickets
    def generate_receipt(self):
        print("="*50)
        print("         MOVIE BOOKING RECEIPT")
        print("="*50)
        print(f"Customer Name: {self.customer.customer_name}")
        print(f"Movie Name: {self.movie.movie_name}")
        print()
        print(f"Ticket Price: rs{self.movie.ticket_price}")
        print(f"Tickets Booked: {self.number_of_tickets}")
        print("-"*50)
        print(f"Total Amount: rs{self.calculate_amount()}")
        print(f"Booking Status:{'CONFIRMED' if self.booking_status else 'PENDING'}")
        print("="*50)
cust = Customer("Noah")
mov = Movie("Avengers",200)
book = Booking(cust, mov, 4)
book.book_ticket()
book.generate_receipt()

# placement eligibility
class Student:
    def __init__(self, sid, sname, atd):
        self.sid=sid
        self.sname=sname
        self.atd=atd
class Assessment:
    def __init__(self, ass_sco):
        self.ass_sco=ass_sco
class PlacementManager:
    def __init__(self):
        self.students = []
    def add_student(self, student, assessment):
        self.students.append((student, assessment))
    def check_eligibility(self, student, assessment):
        return student.atd >= 75 and assessment.ass_sco >= 60
    def generate_report(self, student, assessment):
        status = "ELIGIBLE" if self.check_eligibility(student, assessment) else "NOT ELIGIBLE"
        print("=" * 50)
        print("       PLACEMENT ELIGIBILITY REPORT")
        print("=" * 50)
        print()
        print(f"Student ID       : {student.sid}")
        print(f"Student Name     : {student.sname}")
        print()
        print(f"Attendance       : {student.atd}%")
        print(f"Assessment Score : {assessment.ass_sco}")
        print()
        print(f"Placement Status : {status}")
        print()
        print("=" * 50)
student = Student("S101", "Ava", 85)
assessment = Assessment(78)
manager = PlacementManager()
manager.add_student(student, assessment)
manager.generate_report(student, assessment)

