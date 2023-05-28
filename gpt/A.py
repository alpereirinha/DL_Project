import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df_zero_shot = pd.read_csv('few_shot.csv')

total_acertos = 0

for index, row in df_zero_shot.iterrows():
    predito = row['sentiment']
    verdadeiro = row['sentiment_nltk']
    
    if predito == verdadeiro:
        total_acertos += 1

print("Número total de acertos:", total_acertos)
print("Accuracy:", total_acertos / len(df_zero_shot))
