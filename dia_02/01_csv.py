# %%

import pandas as pd

# %%
# Leitura arquivo
path = '../data/clientes.csv'
df = pd.read_csv(path)
df

# %%

#Salvar arquivo em .csv
df.to_csv("clientes.csv", index = False)

# %% 
#Salvando em arquivo .parquet
df.to_parquet("Clientes.parquet", index = False)

# %%

#Lendo parquet
df_2 = pd.read_parquet("Clientes.parquet")

df_2