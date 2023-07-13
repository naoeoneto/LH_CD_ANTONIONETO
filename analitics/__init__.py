import pandas as pd
import numpy as np
from pandasgui import show
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


cars_train_path = "./input/cars_train.csv"
df = pd.read_csv(cars_train_path, sep="\t")
# show(df)

# Qual o melhor estado cadastrado na base de dados para se vender um
# carro de marca popular e por quê?
features_a = ["marca", "estado_vendedor", "preco"]
brands = ["CHEVROLET", "CITROËN", "FIAT", "PEUGEOT", "RENAULT", "TOYOTA", "VOLKSWAGEN"]
search_a = df[features_a]
search_a_two = search_a[
    (
        (search_a["marca"] == "CHEVROLET")
        | (search_a["marca"] == "CITRÖEN")
        | (search_a["marca"] == "FIAT")
        | (search_a["marca"] == "FORD")
        | (search_a["marca"] == "PEUGEOT")
        | (search_a["marca"] == "RENAULT")
        | (search_a["marca"] == "TOYOTA")
        | (search_a["marca"] == "VOLKSWAGEN")
    )
].loc[search_a["preco"] < 50000]
list_a = search_a_two.drop(["preco"], axis=1)
list_a_final = (
    list_a.groupby("estado_vendedor").count().sort_values(by=["marca"], ascending=False)
)

# Qual o melhor estado para se comprar uma picape com transmissão
# automática e por quê?
features_b = ["tipo", "cambio", "estado_vendedor"]
search_b = df[features_b]
search_b_one = search_b.loc[search_b["tipo"] == "Picape"].loc[
    search_b["cambio"] == "Automática"
]
list_b = search_b_one.drop(["cambio"], axis=1)
list_b_final = (
    list_b.groupby("estado_vendedor").count().sort_values(by=["tipo"], ascending=False)
)

# Qual o melhor estado para se comprar carros que ainda estejam
# dentro da garantia de fábrica e por quê?
features_c = ["estado_vendedor", "garantia_de_fábrica"]
search_c = df[features_c].dropna(axis=0)
list_c = (
    search_c.groupby("estado_vendedor")
    .count()
    .sort_values(by=["garantia_de_fábrica"], ascending=False)
)


cars_test_path = "./input/cars_test.csv"
df_test = pd.read_csv(cars_test_path, encoding="utf-16", sep="\t")
df.fillna(value=None, method="bfill")

features = [
    "num_fotos",
    "hodometro",
    "ano_de_fabricacao",
    "ano_modelo",
    "tipo",
    "tipo_vendedor",
    "ipva_pago",
    "veiculo_licenciado",
]
X = df[features]
y = df["preco"]

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, test_size=0.2, random_state=0
)


def score_dataset(train_x, val_x, train_y, val_y):
    model = RandomForestRegressor(n_estimators=10, random_state=1)
    model.fit(train_x, train_y)
    preds = model.predict(val_x)
    return mean_absolute_error(val_y, preds)


missing_values_col = [col for col in X_train.columns if X_train[col].isnull().any()]
categorical_cols = [
    col_name
    for col_name in X_train.columns
    if X_train[col_name].nunique() < 10 and X_train[col_name].dtype == "object"
]
numerical_cols = [
    col_name
    for col_name in X_train.columns
    if X_train[col_name].dtype in ["int64", "float64"]
]

cols = categorical_cols + numerical_cols
X_train_final = X_train[cols].copy()
X_valid_final = X_valid[cols].copy()

s = X_train.dtypes == "object"
object_cols = list(s[s].index)

X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()
print(X_train_plus.shape)

cars_imputer = SimpleImputer(strategy="constant", add_indicator=True)
imputed_X_train = pd.DataFrame(cars_imputer.fit_transform(X_train_plus))
imputed_X_valid = pd.DataFrame(cars_imputer.transform(X_valid_plus))
print(imputed_X_train.shape)

imputed_X_train.columns = X_train_plus.columns
imputed_X_valid.columns = X_valid_plus.columns

print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))
