#tryexception
print("Program starts")
a=10
print("a=",a)
try:
    print(a/0)
except ZeroDivisionError as e:
    print('not possibleto dividbewith zero if you divide it gives',e)
print('program ends')

# ifelse exception
age=int(input('Enter the age : '))
if(age>=18):
    print("Eligible to vote")
else:
    raise Exception ('Not eligible to vote')

#withdrawal
balance = 5000
try:
    amount = int(input("Enter withdrawl amount: "))
    if amount  > balance:
        raise ValueError("Insufficient Balance")
    print("Withdrawl Successful")
except ValueError as e:
    print("Transactions Failed:",e)

#value error
try:
    monthly_sal=float(input("enter monthly salary: "))
    if(monthly_sal<=0):
        raise ValueError
    annual_sal=monthly_sal*12
    print("Annual salary: ",annual_sal)
except ValueError:
    print("Please enter a valid salary amt")

#atm pin
pin=input("enter the password")
try:
    if(pin=='1234'):
        print('login is successful')
    else:
        raise TypeError('incorrect password')
except TypeError as e:
    print(e)

#finally block
a=10
try:
    print(a)
finally:
    print('finally block code') 