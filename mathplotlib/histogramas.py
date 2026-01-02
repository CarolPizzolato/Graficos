import matplotlib.pyplot as plt
import numpy as np

n = np.random.randn (10000)
'''randn pertence ao random'''


fig, axes = plt.subplots (1,2, figsize = (12,4))


'''aqui estão os eixos:'''

axes[0].hist(n,color = 'y')

'''titulo e eixos'''
axes[0].set_title("Histograma padrão")
axes[0].set_xlim((min(n), max(n)))


axes[1].hist(n,color = 'r',cumulative = True, bins = 50)
axes[1].set_title("Histograma cumulativo")
axes[1].set_xlim((min(n), max(n)))
plt.show()