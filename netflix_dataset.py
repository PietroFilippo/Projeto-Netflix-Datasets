import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')

# carregamento e limpeza de dados
df.dropna(inplace=True)

df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

#análise exploratória de dados
content_type_counts = df['type'].value_counts()
country_counts = df['country'].value_counts()
rating_counts = df['rating'].value_counts()
director_counts = df['director'].value_counts().head(10)  
release_year_counts = df['release_year'].value_counts()

#criação dos gráficos e das tabelas
content_type_counts.plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal')
plt.title('Distribuição de conteúdo(filmes/shows de TV)')
plt.show()
content_type_df = pd.DataFrame({'Content Type': content_type_counts.index, '': content_type_counts.values})
content_type_df.to_csv('content_distribution.csv', index=False)

top_countries = country_counts.head(10)
top_countries.plot(kind='bar')
plt.xlabel('País de origem')
plt.ylabel('Quantidade de conteúdo')
plt.title('Top 10 Países de origem com mais conteúdo')
plt.show()
top_countries_df = pd.DataFrame({'Country': top_countries.index, 'Count': top_countries.values})
top_countries_df.to_csv('top_countries.csv', index=False)

rating_counts.plot(kind='bar')
plt.xlabel('Classificação')
plt.ylabel('Quantidade de conteúdo')
plt.title('Classificações de conteúdo')
plt.show()
rating_df = pd.DataFrame({'Rating': rating_counts.index, 'Count': rating_counts.values})
rating_df.to_csv('rating_distribution.csv', index=False)

director_counts.plot(kind='bar')
plt.xlabel('Diretor')
plt.ylabel('Quantidade de títulos')
plt.title('Diretores mais prolíficos na netflix')
plt.xticks(rotation=45)  
plt.show()
director_counts_df = pd.DataFrame({'Director': director_counts.index, 'Count': director_counts.values})
director_counts_df.to_csv('director_counts.csv', index=False)

release_year_counts.sort_index().plot(kind='bar', figsize=(12, 6))
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade de conteúdo')
plt.title('Distribuição de ano de lançamento')
plt.show()
release_year_counts_df = pd.DataFrame({'Release Year': release_year_counts.index, 'Count': release_year_counts.values})
release_year_counts_df.to_csv('release_year_distribution.csv', index=False, header=['Release Year', 'Count'])
