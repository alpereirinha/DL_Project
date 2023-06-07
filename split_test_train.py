import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('labeled_lyrics_cleaned.csv', encoding='utf-8')

# Dividir os dados em treinamento e dados temporários
train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)
original_data = df.to_csv('original_data.csv', index=False)
test_data1 = test_data[['seq', 'sentiment']]

train_data = train_data.dropna()
# Gravar o DataFrame com todas as colunas em um arquivo CSV
train_data.to_csv('train.csv', index=False)

test_data1 = test_data1.dropna()
# Gravar o DataFrame com apenas as colunas 'seq' e 'sentiment' em um arquivo CSV
test_data1.to_csv('test.csv', index=False)