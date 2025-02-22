import numpy as np
arr1=np.arange(12).reshape(3,4)
print(arr1.ndim)
arr2=np.ones(shape=(2,4),dtype=float)
print(arr2)
arr3=np.ones_like(arr1)
print(arr3)
arr4=np.arange(start=1,stop=14,step=3)
print(arr4)
stu=np.dtype([("name","U10"),("age","i2")])
stus=np.array(object=[("Tom",99),("cauchy",9)],dtype=stu)
print(stus)
print(stus[0][1])
for ele in arr1.flat:
    print(ele,end=" ")
print("\r")    
for row in arr1:
    for ele in row:
        print(ele,end=" ")


