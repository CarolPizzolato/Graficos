import matplotlib.pyplot as plt
import numpy as np

Dia20_03 = (24,27,28,24,21,19,18,17)
Horas = (11,14,17,20,23,2,5,8)


fig = plt.figure(figsize = (6,4))

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.bar(Horas, Dia20_03, alpha = 0.7, color = 'r')
axes1.set_title("Grafico de temperaturas dia 20/03 ")
axes1.set_xlabel("Horas")
axes1.set_ylabel("Temperatura")
plt.show()