#number of correct predictions / number of total lyrics

import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df_zero_shot = pd.read_csv('zero-shot.csv')

total_acertos = 0

for predito, verdadeiro in zip(df_zero_shot['sentiment'], df_zero_shot['sentiment_nltk']):
    if predito == verdadeiro:
        total_acertos += 1

print("Número total de acertos:", total_acertos)
