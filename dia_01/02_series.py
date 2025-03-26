# %%
# Utilizando Python puro

idades = [32,38,30,30,31,
          35,25,29,31,37,
          27,23,36,33,32
]


media = sum(idades) / len(idades)

print("Media:",media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades) - 1)

print ("Variância:",variancia)


# %%

# Usando Pandas

import pandas as pd

# Estatisticas da Séries

series_idades = pd.Series(idades)

media_idades = series_idades.mean()

print("Media idades:", media_idades)

variancia_idades = series_idades.var()

print("Variância:", variancia_idades)

summary_idades = series_idades.describe()

print("Summary idades:", summary_idades)