# %% 
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados tabulares

# %%
# Lê o arquivo CSV separado por ponto e vírgula localizado em "../data/ipea"
df = pd.read_csv("../data/ipea/consolidado_2.csv", sep=";")

# %%
df  # Exibe todo o DataFrame carregado

# %%
# Realiza a transformação de formato:
# - Define "nome" e "período" como índices para agrupar corretamente os dados.
# - Usa stack() para transformar as colunas de métricas em uma única coluna, criando um formato longo (long format).
# - Usa reset_index() para desfazer a hierarquia de índices criada, voltando a um DataFrame plano.
df_stack = (
    df.set_index(["nome", "período"])
      .stack()
      .reset_index()
)

# %%
# Renomeia as colunas do novo DataFrame para refletir a estrutura:
# "nome" e "periodo" continuam, "metricas" representa o que era o nome das colunas, e "valor" é o conteúdo associado.
df_stack.columns = ['nome', 'periodo', 'metricas', 'valor']

# %%
df_stack.head()  # Exibe as primeiras linhas do DataFrame transformado para formato longo

# %%
# Converte o DataFrame empilhado (long format) de volta para o formato original (wide format) usando pivot_table:
# - 'values' define a coluna de valores numéricos ("valor").
# - 'index' define as chaves únicas ("nome" e "periodo") para o agrupamento.
# - 'columns' define a dimensão que se tornará novas colunas ("metricas").
# - reset_index() garante que o índice final volte a ser simples e o DataFrame fique organizado.
(df_stack.pivot_table(values="valor",
                      index=["nome", "periodo"],
                      columns="metricas")
          .reset_index())

# %%
df_stack.head()  # Exibe novamente o DataFrame em formato longo
# %%
# Criação de uma tabela pivô a partir do DataFrame df_stack.
# O objetivo deste código é:
# 1. Transformar o DataFrame de forma que a coluna "nome" se torne o índice das linhas.
# 2. Fazer com que cada valor distinto na coluna "metricas" seja representado por uma coluna na tabela resultante.
# 3. Para cada combinação de "nome" e "metricas", os valores da coluna "valor" serão agregados utilizando a função de agregação "min", ou seja, o valor mínimo será utilizado.
# 4. A função .reset_index() é usada para "resetar" o índice, ou seja, transformar o índice "nome" (que estava como parte do índice hierárquico) em uma coluna normal.
# 
# Por que você removeu a coluna "periodo" do índice?
# - A coluna "periodo" foi removida do índice porque, ao aplicar a transformação para a tabela pivô, você desejou simplificar a estrutura do índice. 
#   Ao manter "periodo" no índice, a tabela resultante teria um índice hierárquico (MultiIndex), o que pode ser mais complexo de manipular e analisar.
# - O objetivo é obter uma tabela mais simples, onde "nome" seja o único índice, e as métricas se tornem as colunas. Isso pode ser útil quando você não precisa da segmentação temporal (ou de "periodo") para a análise ou quando deseja agregar os dados de forma mais direta.
# 
# Objetivo:
# - O código visa reorganizar os dados para que, para cada "nome", as métricas sejam representadas como colunas e os valores agregados por "min" (mínimo). Isso pode ser útil em cenários onde você quer analisar o valor mínimo para cada métrica dentro de cada grupo de "nome", sem manter o índice "periodo".
# 
# Esse processo é especialmente útil para simplificar a visualização e análise de dados agregados em um formato mais amplo, onde a segmentação por "periodo" não é necessária para a análise final.
(df_stack.pivot_table(values="valor",  
                      index=["nome"],  # "nome" se torna o índice (linhas).
                      columns="metricas",  # "metricas" se tornam as colunas.
                      aggfunc="min")  # Função de agregação: pegar o valor mínimo para cada combinação de "nome" e "metricas".
         .reset_index())  # Reinicializa o índice para torná-lo uma coluna regular.

                
