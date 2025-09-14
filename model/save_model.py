import os, pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Caminho do CSV
CSV_PATH = 'data/desafio_indicium_imdb.csv'
os.makedirs('model', exist_ok=True)

# 1) Carregar e preparar
df = pd.read_csv(CSV_PATH)
df = df.dropna(subset=['IMDB_Rating','Meta_score','Gross']).copy()

# Gross numérico simples (sem regra extra)
df['Gross'] = df['Gross'].astype(str).str.replace(',', '', regex=False).astype(float)

# Explode gênero → 1 filme vira várias linhas
df = df.assign(Genre=df['Genre'].astype(str).str.split(',')).explode('Genre')
df = df.dropna()

# Features / target
X = df.drop(columns=['IMDB_Rating','Series_Title','Overview'], errors='ignore')
y = df['IMDB_Rating']

numeric_features = ['Meta_score','No_of_Votes','Gross']
categorical_features = [
    'Released_Year','Runtime','Certificate','Genre',
    'Director','Star1','Star2','Star3','Star4'
]

numeric = Pipeline([('scaler', StandardScaler())])
try:
    onehot = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
except TypeError:
    onehot = OneHotEncoder(handle_unknown='ignore', sparse=False)
categorical = Pipeline([('onehot', onehot)])

pre = ColumnTransformer([
    ('num', numeric, numeric_features),
    ('cat', categorical, categorical_features)
])

model = Pipeline([
    ('pre', pre),
    ('reg', LinearRegression())
])

# 2) Split e treino
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, pred):.4f}")

# 3) Salvar modelo
OUT = 'model/modelo.pkl'
with open(OUT, 'wb') as f:
    pickle.dump(model, f)
print(f"Modelo salvo em {OUT}")
