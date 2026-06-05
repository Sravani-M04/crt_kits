#p1
age=int(input("Enter your age: "))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")
#ternary operator
res="eligible" if age>=18 else "not eligible"
print("you are",res,"to vote")

#p2
num=int(input("Enter a number:"))
if (num>0):
    print("{num} is positive")
elif(num<0):
    print("{num} is negative")
else:
    print("{num} is zero")

#p3
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if(a>b):
    print("a largest no")
else:
    print("b is largest no")

#p4
month=int(input("enter month number"))
if(month>=1 and month<=12):
    print(month,"is valid")
else:
    print(month,"is not valid")

#p5
month=int(input("enter month number:"))
if(month in [1,3,5,7,8,10,12]):
    print("31 days")
elif(month in [4,6,9,11]):
    print("30 days")
elif(month==2):
    print("28 or 29 days")
else:
    print("invalid month")

#p6
a=int(input("enter a value:"))
if(a%2==0):
    print(f"{a} is even")
else:
    print(f"{a} is odd")

#p7
year=int(input("Enter year"))
if(year%4==0 & year%100!=0) or  (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

#p8
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
if(a>=b & a>=c):
    largest=a
elif(b>=a & b>=c):
    largest=b
else:
    largest=c

print("largest number is",largest)

#9
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
if(a<=b & a<=c):
    smallest=a
elif(b<=a & b<=c):
    smallest=b
else:
    smallest=c

print("smallest number is",smallest)

#10
a=int(input("Enter a value"))
b=int(input("Enter b value"))
if(a<b):
    small=a
else:
    small=b
print("small num is",small)

#11
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
if (a>=b and a<=c) or (a<=b and a>=c):
    middle = a
elif (b >= a and b <= c) or (b<=a and b>=c):
    middle = b
else:
    middle = c

print("Middle number is:", middle)

#12
amt=int(input("enter the amt:"))
if(amt>500):
    discount=amt*0.9
    print(f"your amt is above 500, you have 10% discount the total amt is{discount}")
else:
    print(f"your amt is below 500, you don't get discount")