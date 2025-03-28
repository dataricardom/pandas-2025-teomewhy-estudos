# %%

import pandas as pd
import numpy as np
# %%

# Carregando os dados do arquivo CSV

df = pd.read_csv("../data/clientes.csv")

df.head()

# %%

# Adicionando 100 pontos a cada cliente.
# A operação adiciona 100 a cada elemento da coluna "qtdePontos".

df["qtdePontos"] + 100

# Criando uma nova coluna com os pontos ajustados.
# %%
df["pontos_100"] = df["qtdePontos"] + 100

df

# %%

# Atualizando diretamente a coluna "qtdePontos", substituindo os valores antigos pelos novos.

df["qtdePontos"] = df["qtdePontos"] + 100

# %%

# Utilizando um loop for para realizar a mesma operação.
# Essa abordagem é menos eficiente do que a anterior.

nova_coluna = []

for i in df["qtdePontos"]:
    nova_coluna.append(i + 100)

nova_coluna

# %%

df.head()

# %%
# Concatenando informações de duas colunas e armazenando o resultado em uma nova coluna.

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%

# Criando uma nova coluna com a quantidade total de redes sociais associadas ao cliente.

df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()

# %%

# Verificando se o cliente possui todas as redes sociais.
# Caso tenha todas, retorna 1; caso contrário, retorna 0.
# O operador * aplicado a colunas com valores binários (0 e 1) funciona como um AND lógico.


df["todas_Social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()

# %%

# Exibindo estatísticas descritivas da coluna "qtdePontos".

df["qtdePontos"].describe()

# %%
# Aplicando a função logaritmo natural (ln) a todos os valores da coluna "qtdePontos" usando NumPy.
# Caso a coluna contenha valores 0, o logaritmo retornará -inf (infinito negativo).
# Para evitar esse problema, somamos 1 antes de aplicar a função log.

np.log(df["qtdePontos"] + 1)

# %% 

# Aplicando a função exponencial aos valores da coluna "qtdePontos".

np.exp(df["qtdePontos"])

# %%

# Criando uma nova coluna no DataFrame com os valores logarítmicos dos pontos.

df["logPontos"] = np.log(df["qtdePontos"] + 1)

df.head()

# %%
# Usando o Matplotlib para visualizar a distribuição da coluna "qtdePontos" por meio de um histograma.

import matplotlib.pyplot as plt

plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()

# %% 

# Visualizando a distribuição da coluna "logPontos" com um histograma.

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()
