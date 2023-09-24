import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')

# carregamento e limpeza de dados (remover valores nulos)
df.dropna(inplace=True)

#converte date_added para o formato de dia/mes/ano
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

#análise exploratória de dados (conta as informações utilizadas pra os graficos/tabelas)
tipo_conteudo = df['type'].value_counts()
paises = df['country'].value_counts()
classficação = df['rating'].value_counts()
diretores = df['director'].value_counts().head(10)  
ano_lançamento = df['release_year'].value_counts()

#criação dos gráficos e tabelas
#gráfico de pizza
tipo_conteudo.plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal')
plt.title('Distribuição de conteúdo(filmes/shows de TV)')
plt.show()
#converte em um df para converter em csv
tipo_conteudo_df = pd.DataFrame({'Tipo de conteudo': tipo_conteudo.index, '': tipo_conteudo.values})
tipo_conteudo_df.to_csv('tipo_conteudo.csv', index=False)

top_paises = paises.head(10)
#gráfico de barras
top_paises.plot(kind='bar')
plt.xlabel('País de origem')
plt.ylabel('Quantidade de conteúdo')
plt.title('Top 10 Países de origem com mais conteúdo')
plt.show()
top_paises_df = pd.DataFrame({'País': top_paises.index, 'Quantidade': top_paises.values})
top_paises_df.to_csv('top_paises.csv', index=False)

classficação.plot(kind='bar')
plt.xlabel('Classificação')
plt.ylabel('Quantidade de conteúdo')
plt.title('Classificações de conteúdo')
plt.show()
classficação_df = pd.DataFrame({'Classificação': classficação.index, 'Quantidade': classficação.values})
classficação_df.to_csv('classficação.csv', index=False)

diretores.plot(kind='bar')
plt.xlabel('Diretor')
plt.ylabel('Quantidade de títulos')
plt.title('Diretores mais prolíficos na netflix')
#girar os nomes
plt.xticks(rotation=45)  
plt.show()
diretores_df = pd.DataFrame({'Diretores': diretores.index, 'Quantidade': diretores.values})
diretores_df.to_csv('diretores.csv', index=False)

ano_lançamento.sort_index().plot(kind='bar', figsize=(12, 6)) #auemntar o tamanho do gráfico
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade de conteúdo')
plt.title('Distribuição de ano de lançamento')
plt.show()
ano_lançamento_df = pd.DataFrame({'Ano de lançamento': ano_lançamento.index, 'Quantidade': ano_lançamento.values})
ano_lançamento_df.to_csv('ano_lançamento.csv', index=False, header=['Ano de lançamento', 'Quantidade'])