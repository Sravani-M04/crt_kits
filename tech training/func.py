#zero parameterized func
def greet():
    print("Hello, welcome to demo!")
greet()
greet()
greet()

#parameterized func
def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
add(5,8)
add(85,97)

def add(a,b):
    return a+b
print(add(5,8))
print(add(85,97))

#multi func
def add(a,b):
    print(f"addition of {a} and {b} is {a+b}")
def sub(a,b):
    print(f"subtraction of {a} and {b} is{a-b}")
def mul(a,b):
    print(f"multiplication of {a} and {b} is {a*b}")
def div(a,b):
    print(f"division of {a} and {b} is {a/b}")
def rem(a,b):
    print(f"remainder of {a} and {b} is{a%b}")
while True:
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Reminder")
    print("6.Exit")
    print("---------------------------")
    choice=int(input("enter your choice"))
    if choice==6:
        break
    a=int(input("enter first num: "))
    b=int(input("enter second num: "))
    if choice==1:
        add(a,b)
    elif choice==2:
        sub(a,b)
    elif choice==3:
        mul(a,b)
    elif choice==4:
        div(a,b)
    elif choice==5:
        rem(a,b)
    else:
        print("\n")


