# %%

import pandas as pd

# %%

# Carregando os dados do arquivo CSV
clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%
# Ordenando a coluna "qtdePontos" em ordem crescente.
clientes["qtdePontos"].sort_values()

# %%
# Buscando o cliente com o maior número de pontos.

max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %% 

# Ordenando o DataFrame em ordem crescente (padrão).

clientes.sort_values(by="qtdePontos")

#%%

# Ordenando o DataFrame em ordem decrescente.
clientes.sort_values(by="qtdePontos", ascending=False)

# %%
# Obtendo os 5 clientes com mais pontos.
# O método sort_values retorna um novo DataFrame ordenado.

clientes.sort_values(by="qtdePontos", ascending=False).head()

# %%

# Ordenando por pontos e pegando apenas o ID dos clientes com mais pontos.

(clientes.sort_values(by="qtdePontos", ascending=False)
            .head(5)["idCliente"]
)

# %%

# Criando um DataFrame de exemplo com informações de funcionários.

brinquedo = pd.DataFrame(
    {
        "nome": ["Capu", "Pitchula", "Lilo", "Ingrid"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533]
    }
)

brinquedo

# %%

# Ordenando pelo salário e, em caso de empate, pela idade (do maior para o menor).

brinquedo.sort_values(by=["salario", "idade"], ascending=False)

# Ordenando de forma mista: salário em ordem decrescente e idade em ordem crescente.

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
