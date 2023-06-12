import pandas as pd

df = pd.read_csv('./results-gpt/gpt-results.csv')

total_acertos_zero_shot = 0
total_acertos_one_shot = 0
total_acertos_few_shot = 0

for index, row in df.iterrows():
    predito_zero_shot = row['zero_shot']
    predito_one_shot = row['one_shot']
    predito_few_shot = row['few_shot']
    verdadeiro = row['sentiment']
    
    if predito_zero_shot == verdadeiro:
        total_acertos_zero_shot += 1
    
    if predito_one_shot == verdadeiro:
        total_acertos_one_shot += 1
    
    if predito_few_shot == verdadeiro:
        total_acertos_few_shot += 1

total_linhas = len(df)

accuracy_zero_shot = total_acertos_zero_shot / total_linhas
accuracy_one_shot = total_acertos_one_shot / total_linhas
accuracy_few_shot = total_acertos_few_shot / total_linhas

print("Acurácia Zero Shot:", accuracy_zero_shot)
print("Acurácia One Shot:", accuracy_one_shot)
print("Acurácia Few Shot:", accuracy_few_shot)

