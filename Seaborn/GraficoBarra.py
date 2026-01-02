import pandas as pd
import matplotlib.pyplot as plt
'''
x1 = [2,4,6,8,10]
y1 = [6,78,2,4,6]

plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()


x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x1, y1, label = 'Barras 2', color = 'blue')
plt.bar(x2,y2, label = "Lista 2", color = 'yellow')
plt.legend()
plt.show()
'''

idades = [9,58,20,37,97,46,5,6,7,8,3,4,1,2,3,4,5,6,7,8]

ids = [x for x in range(len(idades))]
bins = [x for x in range(0,130,10)]
#plt.hist (idades,bins, histtype = 'bar', rwidth = 0.8)
plt.hist(idades,bins, histtype= 'stepfilled', rwidth= 0.8)
plt.show()

