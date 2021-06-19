# Постройте на одном графике две кривые y(x) для функции двух переменных y(k,x)=cos(k∙x),
# взяв для одной кривой значение k=1, а для другой – любое другое k, не равное 1.
# Для построения использовала PyCharm с Jupiter Notebook пока не знакома
from matplotlib import pyplot as plt
import numpy as np


x = np.arange(0, 20, 0.1)
k1 = 1
k2 = 3
plt.plot(x, np.cos(k1*x), c='y')
plt.plot(x, np.cos(k2*x), c='g')
plt.show()