# %%

import pandas as pd

# %%

df = pd.read_csv('../data/transacoes.csv')
df

# %%

# Dando uma breve investigada
#Verifica quantidade de linhas e colunas. (182835,5)

df.shape

# %%

#Verifica a quantidade de memoria utilizada.
# 53.2MB

df.info(memory_usage='deep')

# %%

#Tipagem de cada coluna.

df.dtypes

# %%

#Renomeia coluna

#O parametro columns utiliza um dicionario onde a chave é o nome da coluna a ser modificada e o valor o novo nome.
rename_column = {
    "descSistemaOrigem": "SistemaOrigem",
}

# Maneira usando variavel.

df.rename(columns = rename_column)

# %%
df_1 = df.rename(columns={"qtdePontos":"qtPontos"})

# %%
#Altera o proprio dataframe sem precisar criar outro
df.rename(columns={"qtdePontos":"qtPontos"}, inplace=True)


# %%
df.rename(columns={"qtdePontos":"qtPontos"}, inplace=True)

df_1.head()


# %%

#Retorna uma serie.

df["idCliente"]

#Retorna um Dataframe.

df[["idCliente"]]


# %%
#COMPARANDO FUNÇÕES NO SQL NO PANDAS


# SELECT * FROM df

df

# %%

#SELECT qtPontos FROM df

df[["qtPontos"]]

# %%

#SELECT * FROM df limit 10

df.head(n=10)

# %%

#SELECT idCliente, qtPontos FROM df LIMIT 10

df[["idCliente", "qtPontos"]].head(n=10)

# %%

# Reordenando ordem das colunas: Só colocar na lista de colunas a ordem que deseja.

#SELECT idCliente, idTransacao, qtPontos FROM  df LIMIT 10

df[["idCliente", "idTransacao", "qtPontos"]].head(10)

# %% 
# Ordenando em ordem alfabetica

colunas = list(df.columns)

colunas.sort()

colunas