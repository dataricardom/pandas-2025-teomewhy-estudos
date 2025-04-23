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

