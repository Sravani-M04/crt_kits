for i in range(1,11):
    if(i==5):
        continue
    print(i)

for i in range(1,11):
    if(i==5):
        break
    print(i)

#1
num=5
print(f"multiplication table of {num} with only even multiples")
for i in range(1,11):
    if(i%2==0):
        print(f"{num}x{i}={num*i}")