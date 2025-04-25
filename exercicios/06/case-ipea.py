# %%
import pandas as pd
import os

# %%
# Lendo o arquivo de homicídios totais (todas as raças), separando por ";"
df_homicidio_geral = pd.read_csv("../../data/ipea/homicidios.csv", sep=";")

# Renomeando a coluna 'valor' para 'homicidios' para dar mais clareza ao dado
df_homicidio_geral = df_homicidio_geral.rename(columns={"valor": "homicidios"})

# Exibindo as primeiras linhas do DataFrame
df_homicidio_geral.head()

# %%
# Lendo o arquivo de homicídios de pessoas negras
df_homicidio_negros = pd.read_csv("../../data/ipea/homicidios-negros.csv", sep=";")

# Renomeando a coluna 'valor' para 'homicidios_negros'
df_homicidio_negros = df_homicidio_negros.rename(columns={"valor": "homicidios_negros"})

# Visualizando as primeiras linhas
df_homicidio_negros.head()

# %%
# Para realizar a junção correta entre os dois DataFrames, 
# precisamos definir as mesmas colunas como índice em ambos.

df_homicidio_geral = df_homicidio_geral.set_index(["nome", "período"])
df_homicidio_negros = df_homicidio_negros.set_index(["nome", "período"])

# %%
# Concatenando os dois DataFrames lado a lado (colunas), pois agora possuem os mesmos índices
pd.concat([df_homicidio_geral, df_homicidio_negros], axis=1).head()

# %%
# Criando uma função para automatizar a leitura, renomeação e organização dos arquivos.
# Isso evita repetição de código.

def read_file(nome_arquivo: str):
    df = (
        pd.read_csv(f"../../data/ipea/{nome_arquivo}.csv", sep=";")      # Lê o arquivo CSV
          .rename(columns={"valor": nome_arquivo})                       # Renomeia a coluna 'valor' para o nome do arquivo (mais descritivo)
          .drop(columns="cod", axis=1)                                   # Remove a coluna 'cod' (se existir)
          .set_index(["nome", "período"])                                # Define 'nome' e 'período' como índice
    )
    return df

# %%
# Testando a função com o arquivo de homicídios de pessoas negras
df_negros = read_file("homicidios-negros")
df_negros

# %%
# Usando o módulo 'os' para listar todos os arquivos da pasta.
# Em seguida, vamos ler e transformar todos usando a função `read_file()`,
# salvando cada DataFrame em uma lista.

nomes_arquivos = os.listdir("../../data/ipea/")
dfs = []

for i in nomes_arquivos:
    nome_base = i.split(".")[0]      # Remove a extensão .csv do nome do arquivo
    dfs.append(read_file(nome_base)) # Lê e processa o arquivo com a função

# %%
# Verificando um dos DataFrames processados (por exemplo, o segundo da lista)
dfs[1]

# %%
# Concatenando todos os DataFrames da lista em um único DataFrame final
# - Juntamos pelas colunas (axis=1)
# - Restauramos o índice para que 'nome' e 'período' voltem a ser colunas normais
# - Ordenamos os dados por 'período' e 'nome' para facilitar análise futura

df_homicidios_full = (
    pd.concat(dfs, axis=1)
      .reset_index()
      .sort_values(['período', 'nome'])
)

df_homicidios_full

# %%
# Salvando o DataFrame final consolidado em um novo arquivo CSV
# - Usamos separador ";"
# - Não salvamos o índice (já que ele foi resetado)

df_homicidios_full.to_csv("../../data/ipea/consolidado_2.csv", index=False, sep=";")
