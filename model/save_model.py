import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np

file_path = 'data/teste_indicium_precificacao.csv'
df = pd.read_csv(file_path)

# Calculando os quartis
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)

# Calculando o intervalo interquartil (IQR)
IQR = Q3 - Q1

# Definindo os limites para remoção de outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# print("Q1R:", Q1)
# print("Q3:", Q3)
# print("IQR:", IQR)
# print("Limite Inferior:", limite_inferior)
# print("Limite Superior:", limite_superior)

df = df[(df['price'] >= limite_inferior) & (df['price'] <= limite_superior)]

df = df.dropna(axis=0)
y = df['price']
features = ['id', 'bairro_group', 'bairro', 'latitude', 'longitude', 'room_type', 'minimo_noites', 'numero_de_reviews', 'reviews_por_mes', 'disponibilidade_365']
X = df[features]


label_enc = LabelEncoder()
X['bairro'] = label_enc.fit_transform(X['bairro'])

encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X[['bairro_group', 'room_type']])

X_encoded_df = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(['bairro_group', 'room_type']))
X_encoded_df.index = X.index
X = pd.concat([X, X_encoded_df], axis=1).drop(columns=['bairro_group', 'room_type'])


param_grid = {
    'n_estimators': [10, 50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0, test_size=0.2)


rf_model = RandomForestRegressor(random_state=42)
random_search = RandomizedSearchCV(
    estimator=rf_model,
    param_distributions=param_grid,
    n_iter=10,
    cv=3,
    scoring='neg_root_mean_squared_error',
    n_jobs=-1,
    random_state=42
)
random_search.fit(train_X, train_y)

print("Melhores hiperparâmetros:", random_search.best_params_)

best_rf_model = random_search.best_estimator_
best_rf_model.fit(train_X, train_y)

predictions = best_rf_model.predict(val_X)
mse = mean_squared_error(val_y, predictions)
rmse = np.sqrt(mse)

print(f"Novo RMSE após ajuste dos hiperparâmetros: {rmse:.2f}")


with open('model/modelo.pkl', 'wb') as file:
     pickle.dump({
        'model': best_rf_model,
        'label_enc': label_enc,
        'one_hot_enc': encoder
    }, file)
print("Modelo e encoders salvos com sucesso!")