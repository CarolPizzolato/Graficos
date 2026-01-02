import matplotlib.pyplot as plt
import numpy as np


y = np.linspace (0,10,100)
x = y**2

fig, axs = plt.subplots(1,2,figsize = (12,4))


axs[0].plot(x,y,color = 'r', label ="função y²")
axs[0].set_title("fIGURA 1")

categorias = ["A", "B", "C", "D", "E"]
valores = np.random.randint(10, 50, size=5)
axs[1].bar(categorias, valores, color='b')
axs[1].set_title("Figura 2")

plt.tight_layout()
plt.show()





