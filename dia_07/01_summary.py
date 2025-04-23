# %%

import pandas as pd

# %%

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]

idades = pd.Series(idades)

idades

# %%

#Tipos de Agregação:
#Soma total.
idades.sum()

# %%
# Media.
idades.mean()

# %%
#Valor maximo.
idades.max()

# %%
# Valor minimo.
idades.min()

# %%
#Lista de estatisticas.
idades.describe()

# %%
#Importando dataframe cliente.

clientes = pd.read_csv("../data/clientes.csv")

clientes.head(5)

# %%

clientes[["flTwitch","flYouTube","flBlueSky", "flInstagram", "flEmail"]].sum()

# %%

clientes["flTwitch"].mean()

# %%
#Cria uma variavel com o nome das colunas facilitar.

redes_sociais = ["flTwitch","flYouTube","flBlueSky", "flInstagram", "flEmail"]

clientes[redes_sociais].sum()

# %%
# Usando dtypes como filtro para descobrir quais colunas não são do tipo object.
# Criando um filtro.
filtro = clientes.dtypes == "object"

clientes.dtypes[filtro]

# %%

#Filtrando todos que são diferente de object.

clientes.dtypes[~filtro]

# %%

# Pegando o nome das colunas que são numericas.

clientes.dtypes[~filtro].index.to_list()

# %%

# Mesma ação de forma simplificada:

num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.to_list()