# %%

import pandas as pd
# %%
clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%
#Metodo 1 usando função python.
# Cria uma função para pegar a ultima parte do id no dataframe clientes.
# E adiciona em uma lista.
def pegar_ult_id(id):
    return id.split("-")[-1]

# %%

#Aplicando função.

id_novo = []

for i in clientes["idCliente"]:
    novo = pegar_ult_id(i)
    id_novo.append(novo)

id_novo
#Adicionando dados a uma nova coluna do dataframe
clientes["novo_id"] = id_novo
# %%
clientes

# %%

#Utilizando apply em vez de for para executar função na serie do dataframe.

clientes["idCliente"].apply(pegar_ult_id)