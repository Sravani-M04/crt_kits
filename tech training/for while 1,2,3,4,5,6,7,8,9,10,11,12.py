#p1
for i in range(1,6):
    print("hello world")

#p2
num=int(input("enter a number"))
for i in range(1,num+1):
    print(i)

#p3
num=int(input("enter a number"))
for i in range(num,0,-1):
    print(i)

#4
num=int(input("enter a no"))
for i in range (1,num+1):
    if (i%2==0):
        print(i)
print("-"*35)
for i in range(2,num+1,2):
    print(i)

#5
num=int(input("enter a no"))
for i in range (1,num+1):
    if (i%2!=0):
        print(i)
print("-"*35)
for i in range(1,num+1,2):
    print(i)

#6
num=int(input("enter a number:"))
sum=0
for i in range (1,num+1):
    sum=sum+i
print("the sum of first",num,"numbers is:",sum)

#7
num=int(input("enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("the factorial of",num,"is",fact)


#8
num=int(input("enter a number:"))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

#9
num=int(input("enter a number:"))
print(f"multiplication table of {num}")
for i in range(10,0,-1):
    print(f"{num}x{i}={num*i}")

#10
num=int(input("enter a number"))
for i in range(1,num+1):
    print("-------------")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")

#11
num=int(input("enter a number"))
for i in range(num,0,-1):
    print("-------------")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")

#12
num=int(input("enter a number"))
for i in range(num,0,-1):
    print("-------------")
    for j in range(10,0,-1):
        print(f"{i}x{j}={i*j}")

#while
#p1
num=int(input("enter a number"))
i=1
while(i<=num):
    print(i)
    i+=1