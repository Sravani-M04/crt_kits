#list compre....
List=[i for i in range(2,20,2)]
Set={i for i in range(2,10,2)}
print(List)
print(sorted(Set))

#shallow 
import copy
original=[1,2,3,4,5]
print(original)
new=original #shallow
print(new)
new[0]=100
print(original)
print(new)

#deep copy
import copy
original=[1,2,3,4,5]
print(original)
new=copy.deepcopy(original)   #deep copy
print(new)
new[0]=100
print(original)
print(new)