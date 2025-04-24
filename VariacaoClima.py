import matplotlib.pyplot as plt
import numpy as np

Dias = ['dom','Seg', 'ter','qua', 'qui','sex','sab']
UmaSemanaMax= [28,29,31,31,29,27,26]
UmasemanaMin = [17,17,19,20,18,18,18]


fig,axes = plt.subplots(1,2, figsize = (12,3))
axes[0].plot(range(len(Dias)),UmaSemanaMax, color = 'red')
axes[0].plot(range(len(Dias)),UmasemanaMin, color = 'b')

axes[0].set_xlabel("Dias da Semana")
axes[0].set_ylabel("Temperatura (°C)")
axes[0].set_title("Temperaturas Máximas e Mínimas")
axes[0].legend()

ProximaSemanaMax = [30, 28, 32, 33, 31, 29, 27]
ProximaSemanaMin = [18, 19, 20, 21, 19, 18, 17]

axes[1].plot (range(len(Dias)),ProximaSemanaMax, color = 'r' )
axes[1].plot (range(len(Dias)),ProximaSemanaMin, color = 'r' )

axes[1].set_ylabel ("Temperaturas em (*C)")
axes[1].set_xlabel("Dias da semana")
axes[1].set_title("Proxima semana")
plt.show()


