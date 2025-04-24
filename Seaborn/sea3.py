import seaborn as sea
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")


df = pd.DataFrame()
df['idade'] = random.sample(range(20,100),30)
df['peso'] = random.sample(range(55,150),30)
print (df.shape)

#sea.lmplot(data = df, x = 'idade', y = 'peso', fit_reg = True)

sea.violinplot(df.idade, color = 'r')
plt.show()
