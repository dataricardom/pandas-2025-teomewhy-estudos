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

# %%

uf

# %%

uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(convert_str_to_float)

uf

# %%

uf["PIB (2015)"] = uf["PIB (2015)"].apply(convert_str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(convert_str_to_float)

uf

# %%

uf.dtypes

# %%

def exp_to_anos(exp):
    return float(exp.replace(",", ".")
                 .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

uf

# %%

por = "86,9%"

def tax_alfabet(por):
    return float(por.replace(",", ".")
      .replace("%", "")) / 100

tax_alfabet(por)
# %%

por = "86,9‰"
def tax_mortalidade(por):
    return float(por.replace(",", ".")
      .replace("‰", "")) / 1000
tax_mortalidade(por)

# %%

uf["Mortalidade infantil (2016)"].head(5)

# %%
uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(tax_mortalidade)
uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(tax_alfabet)
uf

# %%

uf.head(5)
# %%

def est_regioes(uf):
    if uf in ["Distrito Federal","Goiás","Mato Grosso", "Mato Grosso do Sul"]:
        return "Região Centro-Oeste"
    elif uf in ["Alagoas","Bahia","Ceará","Maranhão","Paraíba","Pernambuco","Piauí","Rio Grande do Norte","Sergipe"]:
        return "Região Nordeste"
    elif uf in ["Acre","Amapá","Amazonas","Pará","Rondônia","Roraima","Tocantins"]:
        return "Região Norte"
    elif uf in ["Espírito Santo","Minas Gerais","Rio de Janeiro","São Paulo"]:
        return "Região Sudeste"
    elif uf in ["Paraná","Rio Grande do Sul","Santa Catarina"]:
        return "Região Sul"
    
uf["Regiao"] = uf["Unidade federativa"].apply(est_regioes)

# %%

uf

# %%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (2016)"] < 0.015 and
            linha["IDH (2010)"] > 700)

# %%

uf.apply(classifica_bom, axis = 1)[4]