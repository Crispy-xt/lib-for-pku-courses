import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.randn(4, 4)
print(data)
df = pd.DataFrame(np.abs(data), index=list("abcd"), columns=list("ABCD"))
print(df.plot())
x = np.arange(-5, 5, 0.1)
plt.figure(1)
y = np.sin(x)
plt.plot(x, y)


plt.figure(2)
plt.plot(y, x)

plt.show()
