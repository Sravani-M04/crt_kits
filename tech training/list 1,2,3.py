#p1
Cartoons=['tom and jerry','doremon','shinchan','chota bheem','motu patlu']
print("Accessing the list using positive inbdexing")
print(Cartoons[0])
print(Cartoons[1])
print(Cartoons[2])
print(Cartoons[3])
print(Cartoons[4])
print("Accessing the list using negative inbdexing")
print(Cartoons[-1])
print(Cartoons[-2])
print(Cartoons[-3])
print(Cartoons[-4])
print(Cartoons[-5])

#p2 using for
Cartoons=['tom and jerry','doremon','shinchan','chota bheem','motu patlu']
for i in range(len(Cartoons)):
    print(f"Index{i}:{Cartoons[i]}")
print("----------")
for i in Cartoons:
    print(i)

#p3 using while
Cartoons=['tom and jerry','doremon','shinchan','chota bheem','motu patlu']
i=0
while i<len(Cartoons):
    print(Cartoons[i])
    i+=1

#p4 use deleting
Cartoons=['tom and jerry','doremon','shinchan','chota bheem','motu patlu']
print(Cartoons)
del Cartoons[0]
print(Cartoons)
del Cartoons
print(Cartoons)