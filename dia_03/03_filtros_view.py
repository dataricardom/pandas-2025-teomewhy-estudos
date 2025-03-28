# %% 

import pandas as pd

# %%

df_clientes = pd.read_csv("../data/clientes.csv")

df_clientes

# %%

filtro = df_clientes["qtdePontos"] == 0

#Atribuindo Resultado de um Filtro a uma outra variavel.

cliente_0 = df_clientes[filtro]

cliente_0

# %%

# Se executar da maneira que esta o cliente_0 vai modificar no df_clientes

cliente_0["flag_1"] = 1

# %%

#Agora se eu quiser que mude apenas na nova variavel eu tenho que usar o copy.
# No caso ele cria uma copia do dataframe.

cliente_0 = df_clientes[filtro].copy()

#%%

# E ai sim executar de novo

cliente_0["flag_1"] = 1

cliente_0