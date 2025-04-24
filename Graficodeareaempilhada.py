import matplotlib.pyplot as plt



dias = [1,2,3,4,5,6]
dormir = [7,8,6,5,7,8]
comer = [1,2,3,4,5,5]
trabalhar = [8,7,8,7,9,7]
passear = [8,6,5,4,5,6]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m','c','r','k','b'])
plt.show()