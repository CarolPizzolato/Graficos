import matplotlib.pyplot as plt


fatias = [7,2,2,13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores= ['olive', 'lime', 'violet', 'royalblue']

plt.pie (fatias, labels = atividades, colors= cores, startangle= 90, shadow = False, explode = (0,0,0,0))
plt.show()