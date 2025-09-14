import os, pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

CSV_PATH = 'data/desafio_indicium_imdb.csv'
os.makedirs('model', exist_ok=True)

df = pd.read_csv(CSV_PATH)
df = df.dropna(subset=['IMDB_Rating','Meta_score','Gross']).copy()

df['Gross'] = df['Gross'].astype(str).str.replace(',', '', regex=False).astype(float)
df = df.assign(Genre=df['Genre'].astype(str).str.split(',')).explode('Genre')
df = df.dropna()

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

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, pred):.4f}")

OUT = 'model/modelo.pkl'
with open(OUT, 'wb') as f:
    pickle.dump(model, f)
print(f"Modelo salvo em {OUT}")
