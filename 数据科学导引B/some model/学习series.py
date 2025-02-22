import pandas as pd
import numpy as np
stus=["Tom","Jack","Jerry"]
score=[12,34,56]
name="paper"
s1=pd.Series(data=score,index=stus,dtype=float,name=name)
s2=pd.Series(data={"name":"Tom","age":18,"score":60})
print(s1)
print(s2)
print(s1.value_counts())
data=np.random.randint(low=0,high=10,size=100)
s1=pd.Series(data=data)
print(s1)
print(s1.max())
print(s1.value_counts())
print(s1.var())