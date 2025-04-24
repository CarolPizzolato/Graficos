import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (0,5,10)
y = x ** 2

fig, axes = plt.subplots (1,2,figsize = (10,4))

axes[0].plot(x,x**2,x,np.exp(x))
axes[0].set_title('Escala padrão')
axes[0].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)
axes[1].plot(x,x**2,x,np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title('Escala log')
axes[1].grid(color = 'b', alpha = 1, linestyle = '-', linewidth = 0.9)
plt.show()


