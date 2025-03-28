# %% 

import pandas as pd

# %%

df = pd.read_csv('../data/transacoes.csv')
df.head()

# %% 

# Exemplo python puro para filtrar um determinado valor.

#Percorre uma lista de numeros e retorna valores booleanos de acordo com a condição estabelecida.
#No caso para cada item que for maior ou igual que 50
lista_numeros = [1,2,3,54,90,
                 120,20,25,35,
                 45,51,53,57]
filtro = []
for i in lista_numeros:
    filtro.append(i>=50)

filtro

# %%
# Criado o filtro com resultado booleanos, percorre na lista de numeros
# E compara os valores booleanos True com os numeros na lista e retorna somente os numeros que atendem ao filtro.

resultado = []
for i in range(len(lista_numeros)):
    if filtro[i]:
        resultado.append(lista_numeros[i])
resultado

# %%

# Aplicando Filtros:

teste = pd.DataFrame(

    {
        "nome": ["Ricardo", "Luiz Calors", "Maria Elena"],
        "idade": [29,40,67],
        "uf": ["mg", "rj", "sp"]
    }
)

teste

# %%
# Pega os dados da serie que é a coluna idade, e retorna sim ou não (booleano) de acordo com a condição.
filtro = teste["idade"] >= 18

#Aplica a condição ao dataframe e retorna só os com condição True.

teste[filtro]

# %%

#TRABALHANDO COM DADOS REAIS.

df = pd.read_csv('../data/transacoes.csv')
df.head()

# %%

filtro = df["qtdePontos"] >= 50
filtro
# %%

resultado = df[["qtdePontos"]][filtro].head(10)
resultado

# %%
#Operador and e outros são diferentes no dataframe. E quando há duas condições ou mais tem que usar as condições entre parenteses.
#Filtro Maior ou igual a 50 e menor do que 100.

filtro_maior_50_menor_100 = (df["qtdePontos"] >= 50) & (df["qtdePontos"] < 100)

filtro_maior_50_menor_100
# %%

resultado = df[["qtdePontos"]][filtro_maior_50_menor_100].head(10)
resultado

# %% 

# Operador de filtro OR

#Filtro valores igual a 1 ou maior do que 100.

filtro_igual_1_ou_maior_100 = (df["qtdePontos"] == 1) | (df["qtdePontos"] > 100)

filtro_igual_1_ou_maior_100
# %%

resultado = df[["qtdePontos"]][filtro_igual_1_ou_maior_100].head(10)
resultado

# %%

#Filtro com condição AND com 3 exigências.

filtro = (df["qtdePontos"] > 0) & (df["qtdePontos"] <= 50) & (df["dtCriacao"] >= '2025-01-01')
df[filtro].head()

# %%
#Exemplo de prioridade quando se tem por exemplo and e or e se quer comparar or primeiro.
#Como na matematica se usa parenteses

filtro = (df["qtdePontos"] > 0) & ((df["qtdePontos"] <= 50) & (df["dtCriacao"] >= '2025-01-01'))
df[filtro].head()
