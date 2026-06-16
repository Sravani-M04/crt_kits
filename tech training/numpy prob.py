#0,1,2,3 dimension
import numpy as np
zero=np.array(10)
print(zero)
print(type(zero))
print('dimesion:',zero.ndim)
print("memory: ",zero.nbytes)
one=np.array([12,24,36,48,60])
print(one)
print(type(one))
print('dimesion:',one.ndim)
print("memory: ",one.nbytes)
two= np.array([[12,13,24],[10,20,30]])
print(two)
print(type(two))
print("Dimension :", two.ndim)
print("Memory :",two.nbytes)
three = np.array([[[12,13,14],[10,20,30]],[[23,24,25],[34,35,36]]])
print(three)
print(type(three))
print("Dimension :", three.ndim)
print("Memory :",three.nbytes)

#p2
import numpy as np
a=np.array([1,2,3,4,5])
z=np.zeros(5)
o=np.ones((2,3))
r=np.arange(0,10,2)
l=np.linspace(0,1,5)
rd=np.random.randint(1,100,6)
a+10
a*2
np.sqrt(a)
np.square(a)
np.clip(a,2,4)
np.mean(a)
np.std(a)
np.median(a)
np.percentile(a,75)
a.reshape(5,1)
a.shape
a.dtype
a.astype(float)