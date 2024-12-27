import numpy as np
A=np.array([[-1,-2,1],[0,2.4,1],[1.1,-4,1],[2.4,-1.6,1]])
b=np.array([[-5],[-5.76],[-17.21],[-8.32]])
A_T=A.T
C=np.linalg.inv(A_T@A)
print(C@A_T@b)