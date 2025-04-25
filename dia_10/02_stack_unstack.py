# %% 
import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# %%
# Lê o arquivo CSV separado por ponto e vírgula localizado em "../data/ipea"
df = pd.read_csv("../data/ipea/consolidado_2.csv", sep=";")

# %%
df.head()  # Exibe as primeiras linhas do DataFrame para inspeção inicial

# %%
# Transformação com stack: converte colunas em linhas, criando um formato longo (long format).
# Antes de aplicar o stack, é necessário definir colunas como índice (no caso, "nome" e "período").
# Após o stack, o resultado é uma Series MultiIndex, por isso usamos reset_index() para voltar a um DataFrame.
df_stack = (
    df.set_index(["nome", "período"])  # Define os índices para permitir empilhamento correto
      .stack()                          # Transforma as colunas de métricas em uma coluna única
      .reset_index()                    # Remove os índices hierárquicos, voltando a um DataFrame "normal"
)

# %%
# Renomeia as colunas para nomes mais claros e consistentes
df_stack.columns = ['nome', 'periodo', 'metricas', 'valor']

# %%
df_stack.head()  # Visualiza o DataFrame empilhado (formato longo)

# %%
# Reverte o processo de stack usando unstack, ou seja, retorna ao formato largo (wide format).
# Nesse caso, transformamos os valores únicos da coluna "metricas" em colunas novamente.
df_unstack = (
    df_stack.set_index(["nome", "periodo", "metricas"])  # Define o índice hierárquico necessário para unstack
      .unstack()                                          # Transforma os valores únicos de "metricas" em colunas
      .reset_index()                                      # Reseta os índices para facilitar a visualização
)

# %%
df_unstack.head()  # Exibe o DataFrame após o unstack (formato largo, mas com MultiIndex nas colunas)

# %%
# Após o unstack, as colunas relacionadas às métricas ficam com MultiIndex.
# Aqui removemos o primeiro nível do MultiIndex (que é redundante) e coletamos os nomes das métricas.
metricas = df_unstack.columns.droplevel(0)[2:].tolist()

# %%
# Renomeamos as colunas: as duas primeiras são "nome" e "período", seguidas pelos nomes das métricas.
df_unstack.columns = ["nome", "período"] + metricas

# %%
df_unstack.head()  # Mostra o DataFrame final, limpo, no formato largo e com colunas bem definidas
