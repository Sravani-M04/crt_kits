#1
def disp():
	def show():
		print("show func")
	print("disp function")
	show()
disp()
#2
def one():
	def two():
		print("two")
	print("one")
one()

#3
def washhands():
	print("Washing hands")
def servefood():
	print("serving food")
def eatfood():
	washhands()
	servefood()
	print("Eating food")
	washhands()
eatfood()

#pass a func as parameter
def one(xyz):
    print("first func "+xyz())
def two():
    return "second func"
one(two)

#lambda
def add(a,b):
	return a+b
print(add(5,3))
add=lambda a,b:a+b
print(add(5,3))