import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,10) #grafico de numpy
y = x**2
fig, axes = plt.subplots(nrows = 1, ncols = 2) #cria subgraficos

for ax in axes:
    ax.plot(x,y,'r')
    ax.set_xlabel('eixo x')
    ax.set_ylabel('eixo y')
    ax.set_title('Grafico dividido')
    
fig.tight_layout() #ajusta os espaço entre os subgraficos para melhor visualizacao


plt.show()