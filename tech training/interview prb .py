#1 Reverse a Three-Digit Number
n = int(input())
rev = 0
while n > 0:
    digit = n % 10        
    rev = rev * 10 + digit 
    n = n // 10          
print(rev)

#2 Sum of Digits
n = int(input())
sum_digits = 0
while n > 0:
    sum_digits += n % 10   
    n = n // 10            
print(sum_digits)

#3 Product of Digits
n = int(input())
product = 1
while n > 0:
    product *= n % 10  
    n = n // 10        
print(product)

#4 Swap First and Last Digit
n, d = int(input()), []
while n: 
    d += [n%10]
    n//=10
d[0], d[2] = d[2], d[0]
for i in d[::-1]: n = n*10 + i
print(n)

#5 Sum of First and Last Digit
n = int(input())
first = n // 100    
last = n % 10       
print(first + last)

#6 Extract Individual Digits
n=int(input())
for i in str(n):
    print(i)

#7 Average of Digits
n = int(input())
total = 0
for i in range(3):
    total += n % 10
    n //= 10
print(total // 3)

#8 Largest digit
n = int(input())
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
print(largest)

#9 Smallest Digit
n = int(input())
smallest = 9
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
print(smallest)

#10 Check Palindrome Number
n = int(input())
a = n // 100        
b = n % 10          
if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")

#11 Reverse and Add
n = int(input())
original = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(original + rev)

#12 Reverse and Find Difference
n = int(input())
original = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
diff = original - rev
if diff < 0:
    diff = -diff
print(diff)

#13 Sum of Squares of Digits
n = int(input())
total = 0
while n > 0:
    digit = n % 10
    total += digit * digit
    n //= 10
print(total)

#14 Product of First and Last Digit
n = int(input())
first = n // 100   
last = n % 10      
print(first * last)

#15  Check Increasing Digits
n = int(input())
a = n // 100       
b = (n // 10) % 10 
c = n % 10         
if a < b < c:
    print("Increasing")
else:
    print("Not Increasing")

#16 Check Decreasing Digits
n = int(input())
a = n // 100       
b = (n // 10) % 10 
c = n % 10         
if a > b > c:
    print("Decreasing")
else:
    print("Not Decreasing")

#17 Replace Middle Digit with Zero
n = int(input())
a = n // 100 
b = n % 10 
result = a * 100 + 0 * 10 + b
print(result)

#18 Sum of Even Digits
n = int(input())
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n //= 10
print(total)

#19 Sum of Odd Digits
n = int(input())
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        total += digit
    n //= 10
print(total)

#20 Move Last Digit to Front 
n = input()
print(n[-1] + n[:-1])

#21 Check Armstrong Number (3 Digits)
n = int(input())
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
if hundreds**3 + tens**3 + ones**3 == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

#22 Check Strong Number
import math
n = int(input())
original = n
sum_fact = 0
while n > 0:
    digit = n % 10
    sum_fact += math.factorial(digit)
    n //= 10
print("Strong Number" if sum_fact == original else "Not Strong Number")

#23 Sum of First Two Digits
n = input()
print(int(n[0]) + int(n[1]))

#24. Product of Last Two Digits
n = input()
print(int(n[1]) * int(n[2]))

#25 Check if Sum of Digits is Even
n = int(input())
digit_sum = 0

while n > 0:
    digit_sum += n % 10
    n //= 10
if digit_sum % 2 == 0:
    print("Even")
else:
    print("Odd")

#26 Check if Product of Digits is Greater Than 100
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
if product > 100:
    print("Greater Than 100")
else:
    print("Not Greater Than 100")

#27 Find Greatest Among Three Digits
n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
print(max(a, b, c))

#28 Find Smallest Among Three Digits
n = int(input())
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
print(min(hundreds, tens, ones))

#29 Count Zero Digits
n = int(input())
count = 0
while n > 0:
    if n % 10 == 0:
        count += 1
    n //= 10
print(count)

#30 Check if First and Last Digits are Same
n = int(input())
hundreds = n // 100
ones = n % 10
print("Same" if hundreds == ones else "Not Same")

#31 Sum of Cubes of Digits
n = int(input())
original = n
sum_cubes = 0
while n > 0:
    digit = n % 10
    sum_cubes += digit ** 3
    n //= 10
print(sum_cubes)

#32 Difference Between Sum and Product of Digits
n = int(input())
original = n
digit_sum = 0
product = 1
while n > 0:
    digit = n % 10
    digit_sum += digit
    product *= digit
    n //= 10
difference = digit_sum - product
print(abs(difference)) 

#33. Find Second Largest Digit
n = int(input())
a, b, c = n//100, (n//10)%10, n%10
digits = [a, b, c]
digits.sort()
print(digits[1]) 

#34. Find Second Smallest Digit
n = int(input())
a, b, c = n//100, (n//10)%10, n%10
digits = [a, b, c]
digits.sort()
print(digits[1])

#35 Check if Middle Digit is Largest
n = int(input())
first = n // 100       
middle = (n // 10) % 10 
last = n % 10           
if middle > first and middle > last:
    print("Yes")
else:
    print("No")

#36 Check if Middle Digit is Smallest
n = int(input())
first = n // 100        
middle = (n // 10) % 10 
last = n % 10          
if middle < first and middle < last:
    print("Yes")
else:
    print("No")

#37 Create Number Using Reverse Order of Digits
n = int(input())
reversed_num = int(str(n)[::-1])
print(reversed_num)

#38 Check Divisibility by Sum of Digits
n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
digit_sum = a + b + c
if n % digit_sum == 0:
    print("Divisible")
else:
    print("Not Divisible")

#39 Find Distance Between First and Last Digit
n = int(input())
first = n // 100   
last = n % 10      
diff = abs(first - last)
print(diff)

#40 Digit Transformation
n = int(input())
a = n // 100         
b = (n // 10) % 10   
c = n % 10           
new_num = (a + 1) * 100 + (b + 1) * 10 + (c + 1)
print(new_num)

#41 Check Spy Number
n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
if a + b + c == a * b * c:
    print("Spy Number")
else:
    print("Not a Spy Number")

#42  Double Every Digit
n = int(input())
a, b, c = n//100, (n//10)%10, n%10
print((a*2)*100 + (b*2)*10 + (c*2))

#43 Compare First Digit and Sum of Remaining Digits
n = int(input())
first = n // 100          
second = (n // 10) % 10   
last = n % 10             
if first > second + last:
    print("Greater")
else:
    print("Not Greater")

#44 Create Alternate Number
n = int(input())
first = n // 100          
middle = (n // 10) % 10   
last = n % 10             
new_num = last * 100 + middle * 10 + first
print(new_num)

#45 Check Harshad Number
n = int(input())
temp, digit_sum = n, 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print("Harshad Number" if n % digit_sum == 0 else "Not Harshad Number")

#46 Find Sum of First and Middle Digit
n = int(input())
first = n // 100
middle = (n // 10) % 10
print(first + middle)

#47 Find Product of First and Middle Digit
n = int(input())
first = n // 100
middle = (n // 10) % 10
print(first * middle)

#48  Check if Digits Form an Arithmetic Sequence
n = int(input())
a, b, c = n//100, (n//10)%10, n%10
if b - a == c - b:
    print("Arithmetic Sequence")
else:
    print("Not Arithmetic Sequence")

#49 Check if Digits Form a Geometric Sequence
n = int(input())
a, b, c = n//100, (n//10)%10, n%10
if a != 0 and b != 0 and b/a == c/b:
    print("Geometric Sequence")
else:
    print("Not Geometric Sequence")

#50 Create a Mirror Difference Number
n = int(input())
a, b, c = n//100, (n//10)%10, n%10
reverse = c*100 + b*10 + a
print(abs(n - reverse))

n=int(input())
abc=n//100,n//10,n%10

