# %% 
import pandas as pd

idades = [ 32,38,30,30,31,
          35,25,29,31,37,
          27,23,36,33,39

]

nomes = ['Teo', 'Bruno',
          'Jorge','Ricardo','Luiz',
          'Luiz Carlos', 'Ronal', 'Leticia'
          ,'Tamires', 'Juliana', 'Kayan',
          'Matheus','Chico', 'Pig', 'Maciel']

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)


