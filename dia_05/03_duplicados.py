# %% 
import pandas as pd

# %% 
# Criando um DataFrame com colunas de nome, sobrenome e salário.
df = pd.DataFrame({
    "nome": ["teo", "lara", "nah", "bia", "mah", "lara", "mah", "mah"],
    "sobrenome": ["calvo", "calvo", "ataide", "ataide", "silva", "silva", "silva", "silva"],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
})

df

# %% 
# Removendo linhas duplicadas considerando todas as colunas.
# Por padrão, mantém a primeira ocorrência (mais antiga).
df.drop_duplicates()

# %% 
# Removendo linhas duplicadas, mas mantendo a última ocorrência (mais recente).
df.drop_duplicates(keep='last')

# %% 
# Removendo duplicatas com base apenas nas colunas "nome" e "sobrenome",
# ou seja, se houver pessoas com o mesmo nome completo, apenas uma será mantida.
df.drop_duplicates(subset=["nome", "sobrenome"])

# %% 
# É uma boa prática ordenar os dados antes de remover duplicatas,
# especialmente quando o critério de desempate é algum valor como salário.
# Aqui, ordenamos o DataFrame por salário em ordem decrescente.
df = df.sort_values("salario", ascending=False)
df

# %% 
# Após a ordenação, removemos as duplicatas mantendo a última ocorrência,
# o que significa manter o menor salário entre os duplicados.
df.drop_duplicates(keep='last', subset=["nome", "sobrenome"])

# %% 
# Código final: ordena o DataFrame do maior para o menor salário,
# remove duplicatas baseadas em nome e sobrenome, mantendo a última ocorrência,
# e atualiza o próprio DataFrame com o resultado.
df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(keep='last', subset=["nome", "sobrenome"])
)

df
