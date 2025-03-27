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
    "dtCriacao": "Criacao"
}

# Maneira usando variavel.

df.columns(columns = rename_column)

df_1 = df.rename(columns={"qtdePontos":"qtPontos"})

#Altera o proprio dataframe sem precisar criar outro
df.rename(columns={"qtdePontos":"qtPontos"}, inplace=True)


# %%

df_1.head()


# %%
