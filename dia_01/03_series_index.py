# %% 

import pandas as pd

idades = [ 32,38,30,30,31,
          35,25,29,31,37,
          27,23,36,33,39

]

series_idades = pd.Series(idades)

series_idades


# %%

#Python
idades[0]

#Series Pandas
series_idades[0]

# %%

series_idades[14]


# %%

# Ordenando do menor para o maior

series_idades = series_idades.sort_values()

series_idades

# %%
# Usando iloc para ignorar idex e buscar por posição
series_idades.iloc[0]


# %%
# Usando iloc para ignorar idex e buscar por posição

series_idades.iloc[-1]

# %%

#Usando iloc para buscar os 3 primeiros elementos de uma serie

series_idades.iloc[:3]



# %% 
# Pegando do ultimo ate o primeiro usando iloc


series_idades.iloc[::-1]


# %%

import pandas as pd

idades = [ 32,38,30,30,31,
          35,25,29,31,37,
          27,23,36,33,39

]

indexs = ['Teo', 'Bruno',
          'Jorge','Ricardo','Luiz',
          'Luiz Carlos', 'Ronal', 'Leticia'
          ,'Tamires', 'Juliana', 'Kayan',
          'Matheus','Chico', 'Pig', 'Maciel']

series_idades = pd.Series(idades, index = indexs)

series_idades.iloc[0]

series_idades.iloc[[0]]

# %%

# Iloc ignora o index e busca nas linhas

series_idades.iloc[0]


# Loc usa o index. Não precisa colocar .loc

#São a mesma coisa.

series_idades.loc['Teo']
series_idades['Teo']
