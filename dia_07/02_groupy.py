# %%

import pandas as pd
# %%

transacoes = pd.read_csv("../data/transacoes.csv")

transacoes.head()
# %%

#Usando groupby no dataframe.
# Agrupando por id do cliente, e realizando operação count em todas as colunas do dataframe.

transacoes.groupby(by=["idCliente"]).count().head()

# %%
# Aplicando apenas a uma coluna do dataframe, agrupado por idCliente.
# Retornando uma serie.
transacoes.groupby(by=["idCliente"])["idTransacao"].count()

#Se quiser visualisar como um dataframe é preciso adicionar outro colchete onde tem coluna especificada.
transacoes.groupby(by=["idCliente"])[["idTransacao"]].count()

# %%

# Nos dois exemplos acima a coluna que é a condição do groupy by
# Retorna como idice. Caso queria que retorne como coluna tem que fazer a seguinte modificação.
transacoes.groupby(by=["idCliente"], as_index=False)[["idTransacao"]].count()

# %%
# Usando agg para fazer varias agregações ou uma especifica para cada coluna.
# Para fazer isso se usa a estrutura de dicionario dentro de agg.

(transacoes.groupby(by=["idCliente"], as_index=False)
                .agg({"idTransacao": ["count"],
                 "qtdePontos": ["sum", "mean"]
                 }))

# %%

summary = (transacoes.groupby(by=["idCliente"], as_index=False)
                .agg({"idTransacao": ["count"],
                 "qtdePontos": ["sum", "mean"]
                 }))

summary

# %%

# Descobrindo colunas

summary.columns

# %% 

# o dataframe summary tem uma estrutura de colunas multindex
# O que pode ser visto como um sistema de hiearquia.
# O qual pode ser acessado colocando todas as condições da coluna desejada.
# Da seguinte forma:
summary[("qtdePontos", "mean")]

# %%

# Facilitando o mesmo processo acima:
#Definindo eu mesmo como vai ficar as colunas e acabando com o multindex.
summary.columns = ['idCliente', 'qtdeTransacao', 'totalPontos', 'avgPontos']

summary