import seaborn as sea
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")



import seaborn as sns

dados = sns.load_dataset("tips")
print(dados.head())


sea.lmplot(data = dados, x ="total_bill", y = "tip", col = 'smoker')
plt.show()