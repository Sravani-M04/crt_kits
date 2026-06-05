#p1 append
List=["python","java","c++","javascript"]
print("the original list is:",List)
List.append("ruby")
print("the list after appending :",List)
List.append("sql")
print("the list after appending :",List)

#p2 insert
List=["python","java","c++","javascript"]
print("the original list is:",List)
List.insert(0,"sql")
print(List)
List.insert(1,"ruby")
print(List)
List.insert(2,"cp")
print(List)

#p3 pop
List=["python","java","c++","javascript"]
print("the original list is:",List)
List.insert(0,"sql")
print(List)
List.pop(0)
print(List)

#p4 remove
List=["python","java","c++","javascript"]
print("the original list is:",List)
List.insert(0,"sql")
print(List)
List.remove("c++")
print(List)

#p5 index
List=["python","java","c++","javascript"]
print("the original list is:",List)
print(List.index("java"))
print(List.index("c++"))

#p6 reverse
List=["python","java","c++","javascript"]
print("the original list is:",List)
List.reverse
print("the reversed list is:",List)

#p7 extend
front_end=['HTML','CSS','JS','BootStrap','ReactJS']
lang=['Python','django','Flask','NodeJS','Express']
print("Front-end TECHNOLOGY: ",front_end)
print("Back-end TECHNOLOGY: ",lang)
lang.extend(front_end)
print("All TECHNOLOGY: ",lang)

#p8 count
List=[2,3,4,5,2,2]
print(List.count(2))

#p9 sort
List=[2,3,4,5,2,2]
List.sort()
print(List)
List.reverse()
print(List)

#10 clear
List=[2,3,4,5,2,2]
List.clear()
print(List)

#11 concatination
a=[10,20,30]
b=[1,2,3]
res=a+b
print(res)

#12 repitition
b=[1,2,3]
res=b*3
print(res)