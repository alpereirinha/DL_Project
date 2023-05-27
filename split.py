from sklearn.model_selection import train_test_split

# Split the data into training and temporary data
train_data, test_data = train_test_split(df_en, test_size=0.2, random_state=42)

# Split the temporary data into validation and test sets

# train_data will contain 80% of the data for training
# val_data will contain 10% of the data for validation
# test_data will contain 10% of the data for testing
# Selecionar apenas a coluna desejada
test_data1 = test_data[['LyricsClean','sentiment']]

# Gravar o DataFrame com apenas a coluna desejada em um arquivo CSV

train_data.to_csv('train.csv', index=False)

test_data1.to_csv('test.csv', index=False)

#gpt = pd.read_csv('test_data.csv')

# Selecionar as primeiras 5 linhas
#primeiras_5_linhas = gpt.head(5)

# Gravar as primeiras 5 linhas em um arquivo CSV
#primeiras_5_linhas.to_csv('gpt_test.csv', index=False)