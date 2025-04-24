import matplotlib.pyplot as plt
categorias = ["A", "B", "C", "D"]
valores = [23, 45, 12, 34]

fig = plt.figure(figsize=(6,4))

axs = fig.add_axes ([0.1,0.1,0.8,0.8])
axs.bar(categorias,valores,alpha = 0.7, color = 'r')
axs.set_xlabel(" valores ")
axs.set_ylabel("categorias")
plt.show()



