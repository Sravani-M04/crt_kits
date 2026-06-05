#p1
size=int(input("Enter the size of list: "))
Age=[]
for i in range(size):
    ele=int(input("Enter the age: "))
    Age.append(ele)
print(Age)
for i in Age:
    if(i>=1 and i<=100):
        if(i<12):
            print(f"{i}-----> $10")
        elif(i>=12 and i<=60):
            print(f"{i}------> $15")
        else:
            print(f"{i}-----> $12")

#p2
pin=int(input("enter the pin: "))
acc_bal=0
if pin==1234:
    print("welcome to the bank")
    while True:
        print("1.Deposite")
        print("2.Withdrawal")
        print("3.Balance inquiry")
        print("4.Exit")
        choice=int(input("ewnter your choice: "))
        print("\n")
        if(choice==1):
            amt=int(input("enter amt to deposite: "))
            acc_bal=acc_bal+amt
            print(f"Dear customer your account xxxxxxxx1223 is credited with{amt}")
        elif(choice==2):
            amt=int(input("enter the amt to withdraw: "))
            if(amt<acc_bal):
                print(f"Dear customer your account xxxxxxx1223 is debited with {amt}")
                acc_bal=acc_bal-amt
            else:
                print("Insufficient balance......")
        elif(choice==3):
            print(f"Dear customer your account xxxxxxxxxx1223 has {acc_bal}")
        else:
            print("Thank You.........")
            break
else:
    print("You enter wrong pin")


#p3
size=input("enter the size of pizza: ")
toppings=int(input("enter the number of toopings: "))
size_price={"small": 10, "medium": 15, "large": 20}
topping_price={"cheese":2, "pepperoni":3, "olives":5, "jalapenos":5, "onions":1,"corn":3}
total=size_price[size] 
for i in range(toppings):
    topping=input("enter your topping: ")
    total+=topping_price[topping]
print("Total bill: $", total)

#or

size = input("enter the size of pizza: ")
toppings = int(input("enter the number of toopings: "))
size_price = {"small": 10, "medium": 15, "large": 20}
topping_price = {"cheese": 2, "pepperoni": 3, "olives": 5, "jalapenos": 5, "onions": 1, "corn": 3}
total = size_price[size]
print("\nBill ")
print(f"Pizza size: {size.title()} - ${size_price[size]}")
for i in range(toppings):
    topping = input("enter your topping: ")
    price = topping_price[topping]
    total += price
    print(f"Topping {i+1}: {topping.title()} - ${price}")
print("Total bill: $", total)

#4
size_price = {"small": 10, "medium": 15, "large": 20}
topping_price = {"cheese": 2, "pepperoni": 3, "olives": 5, "jalapenos": 5, "onions": 1, "corn": 3, "tomatos":4}
num_pizzas = int(input("enter number of pizzas: "))
order_total = 10
for p in range(1, num_pizzas + 1):
    print(f"\nPizzas {p}:")
    size = input("enter the size of pizzas: ")
    n = int(input("enter the number of toppings: "))
    pizzas_total = size_price[size] 
    for i in range(n):
        topping = input("enter your topping: ")
        pizzas_total += topping_price[topping]
    order_total += pizzas_total
    print(f"Pizzas {p} subtotal: ${pizzas_total}")
if order_total < 50:
    delivery = 5
else:
    delivery = 0
grand_total = order_total + delivery
print("\n--- Bill ---")
print("Order value: $", order_total)
print("Delivery charge: $", delivery)
print("Total bill: $", grand_total)

