#p1
num=int(input("enter the number: "))
count=0
rem=0
while(num!=0):
    rem=num%10
    count+=1
    num=num//10
print(f"count of digits is {count}")

#2
num=int(input("enter the number: "))
sum=0
rem=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(f"sum of digits is {sum}")

#3
n=int(input("Enter a number"))
if n<=1:
    print("not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
        else:
            print("prime")

#4
n = int(input("Enter an integer: "))

rev_num = 0

while n != 0:
    digit = n % 10          # get last digit
    rev_num = rev_num * 10 + digit  # add digit to result
    n = n // 10             # remove last digit

print("Reversed integer:", rev_num)

#5
n = int(input("Enter a number: "))

if str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")