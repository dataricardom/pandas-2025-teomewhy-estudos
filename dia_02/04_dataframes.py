# %% 

import pandas as pd

#%%

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes


# %%
#MANEIRAS DE AMOSTRA DE VISUALIZAÇÃO DO DATAFRAME.

# head . É como se fosse o limite do sql. Por padrão, tras as 5 primeiras linhas do dataframe

df_clientes.head()

# %% 
# n . Expecifica o número de linhas que retorna.

df_clientes.head(n=10)

# %%
# tail . Mostra o final do dataframe. Tras as ultimas linhas, 5 ultimos.

df_clientes.tail()

# %%

#sample . Retorna linhas sortidas.

df_clientes.sample(10)

# %%

#ATRIBUTOS PARA VERIFICAR ESPECIFICAÇÕES DO DATAFRAME.

#.shape é um atributo do dataframe e retorna uma tupla. Otima pra descobrir quantas linhas e colunas um dataframe tem.

df_clientes.shape

# %%
#.columns .Retorna o nome das colunas no dataframe.

df_clientes.columns

# %%
#.index .Verifica  quantiade de index

df_clientes.index

# %%

#.info .Retorna detalhes do dataframe.

df_clientes.info()

# %%

#Descobre a quantidade de memoria que o dataframe esta usando.

df_clientes.info(memory_usage='deep')


# %%
#Atributo .dtypes, retorna uma serie onde os valores que estão dentro desta serie são  tipos de cada coluna.

df_clientes.dtypes

# %%
#Buscando a tipagem de uma coluna.

df_clientes.dtypes["idCliente"]

