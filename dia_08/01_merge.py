# %%

import pandas as pd
# %%
# Importando base transacoes
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()
# %%
# Importando base Clientes
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%
#Fazendo left join com o dataframe cliente.
transacoes.merge(
    right=clientes, 
    how='left',
    on=['idCliente'],
    suffixes=['Transacao', 'Clientes']
    )
# %%
# Especificando as colunas que vão se relacionar.

transacoes.merge(
    right=clientes, 
    left_on=['idCliente'],
    right_on=['idCliente'],
    how='left',
    suffixes=['Transacao', 'Clientes']
    )
# %%
