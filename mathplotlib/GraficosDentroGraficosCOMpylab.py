import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,10) #grafico de numpy
y = x**2
fig = plt.figure() #cria a figura

#figura primaria
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Ajuste para centralizar melhor
axes1.plot(x,y, 'r') #criamos o plot, o r é a cor que queremos
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Grafico de linhas')

#figura secundaria
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes2.plot (y,x,'g')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('Figura secundaria')

axes3 = fig.add_axes([0.7,0.3,0.1,0.1])
axes3.plot (y,x,'g')
axes3.set_xlabel('x')
axes3.set_ylabel('y')
axes3.set_title('Figura terciária')

plt.show()