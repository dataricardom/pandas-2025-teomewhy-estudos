# %%

import pandas as pd
# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"


dfs = pd.read_html(url)

uf = dfs[1]

uf

# %%

#Verificando tipo dos dados

uf.dtypes

# %%

numero = "251 529,2"

def convert_str_to_float(num:str):
    num = float(num.replace(" ", "")
                .replace(",",".")
                .replace("\xa0",""))
    return num



convert_str_to_float(numero)


# %%
# Chamando função para fazer transformação na coluna e atribuindo modificação ao dataframe
uf["Área (km²)"]=uf["Área (km²)"].apply(convert_str_to_float)

#%%
#Verificando modificação

uf.dtypes