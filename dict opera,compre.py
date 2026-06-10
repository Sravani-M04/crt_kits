#1
Lang={
    'ui/ux':['html','css','js','react js','express js'],
    'backend':['python','flask','django','pyramid','bottle'],
    'server':['sql','pl-sql','ms-sql']
}
print(Lang['ui/ux'])
print(Lang['backend'])
print(Lang['server'])
Lang['server']=['oracle-sql']
print(Lang['server'])

#2&3 add new id and delete
std={
    101:'scott',102:'miller',103:'adams',104:'james',105:'david'
}
print(std)
std[106]='xyz'
print(std)
del std[101]
del std[106]
print(std)
#check 101,104,105

#4 clear
std={
    101:'scott',102:'miller',103:'adams',104:'james',105:'david'
}
print(std)
std[106]='xyz'
print(std)
std.clear()

#5 key values
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
print(std)
print(std.values())
print(std.keys())

#6 fromkeys
colors={}
keys=(101,102,103)
values=('red','black')
print(colors.fromkeys(keys,values))

#7 get
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
print(std.get(101))
print(std.get(105))

#8 items
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
print(std.items())

#9 update
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
std.update({103:'abc'})
print(std)

#10 pop
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
std.pop(101)
print(std)

#11 popitem
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
std.popitem()
print(std)

#12 set default
std={101:'scott',102:'miller',103:'adams',104:'james',105:'david'}
print(std)
std.setdefault(107,'null')
print(std)

#13 nested list,tuple,dict
list=[[1,2,3],[4,5,6,],[7,8,9]]
for i in list:
    print(i)

tuple=((1,2,3),(4,5,6),(7,8,9))
for i in tuple:
    print(i)

dict={
    'std1':(101,'scott',20),
    'std2':(102,'miller',23)
}
for i in dict:
    print(i,dict[i])

#dict comprehension
dict={i:i*i for i in range(1,11) }
print(dict.items())