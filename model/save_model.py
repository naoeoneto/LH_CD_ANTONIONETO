import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pickle

file_path = 'data/desafio_indicium_imdb.csv'
df = pd.read_csv(file_path)

df = df.dropna(subset=['IMDB_Rating', 'Meta_score', 'Gross'])  # Exemplo
df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
df = df.assign(Genre=df['Genre'].str.split(',')).explode('Genre')
df = df.dropna()

X = df.drop(columns=['IMDB_Rating', 'Series_Title', 'Overview'])
y = df['IMDB_Rating']

numeric_features = ['Meta_score', 'No_of_Votes', 'Gross']
categorical_features = ['Released_Year', 'Runtime', 'Certificate', 'Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4']

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
])

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir modelo de regressão linear
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Treinar modelo
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Avaliar o modelo
mae = mean_absolute_error(y_test, y_pred)
print(f'MAE: {mae}')

# Salvar o modelo em um arquivo .pkl
with open('model/modelo.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Modelo salvo com sucesso!")
