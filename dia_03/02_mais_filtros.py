# %% 

import pandas as pd 

# %%

df = pd.read_csv("..//data/transacao_produto.csv")
df

# %%

#Filtrando produtos com id igual a 5 ou 11. Primeiro exemplo.

filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]

# %%

#Outra maneira de fazer o mesmo que acima.

filtro = df["idProduto"].isin([5,11])

df[filtro]


# %% 
clientes = pd.read_csv("..//data/clientes.csv")
clientes.head()

#%%

#Trabalhando com NOT NULL

#Buscando Clientes que a data de criação tem campo nulo e os que não tem.

#isna pega os nulos

filtro_null = clientes["dtCriacao"].isna()
clientes[filtro_null]

#%%

# " ~ " é o NOT IN.Inverte(Nega) a condição e retorna os valores que não são nulos.

filtro_not_null = ~ clientes["dtCriacao"].isna()


#%%
#notna pega os não nulos.

filtro_not_null = clientes["dtCriacao"].notna()
clientes[filtro_not_null]
