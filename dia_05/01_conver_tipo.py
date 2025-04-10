# %%

import pandas as pd

# %%


clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%

# Convertendo tipo de colunas:
#.astype converte os tipos.

clientes["qtdePontos"].astype(float)

# %%
#.replace substituir um valor especificado por outro.
clientes["dtCriacao"].replace(
    {"0000-00-00 00:00:00.000":
      "2025:03:28 17:00:00.000"
     }
)

# %%

# Modificando Data no Dataframe

clientes["dtCriacao"] = clientes["dtCriacao"].replace(
    {"2025:03:28 17:00:00.000":"2025-03-28 17:00:00.000"
     }
)

# %%

clientes["dtCriacao"]

# %%

# Após corrigido o problema da data 0000:00:00
#Agora pode se aplicar a conversão para data ja alterando no Dataframe original.

clientes["dtCriacao"] = pd.to_datetime(clientes["dtCriacao"])
# %%

clientes["dtCriacao"]

# %%

# Apos convertido para datetime, pode se aplixar funções como dt.

#Pegando o Ano
clientes["dtCriacao"].dt.year

# %%

#Pegando o dia

clientes["dtCriacao"].dt.day


# %%
# Pegando o mês

clientes["dtCriacao"].dt.month

# %%
