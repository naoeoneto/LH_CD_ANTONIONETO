import pandas as pd

cars_train_path = "./input/cars_train.csv"
df = pd.read_csv(cars_train_path, sep="\t")
# print(df.columns)

# Utilizando as variáveis (features), faça um relatório com uma análise das
# principais estatísticas da base de dados. Descreva graficamente essas
# variáveis (features), apresentando as suas principais estatísticas descritivas.
# Comente o porquê da escolha destas estatísticas e o que elas nos informam.


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
# print(list_a_final.head())

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
# print(list_b_final.head())

# Qual o melhor estado para se comprar carros que ainda estejam
# dentro da garantia de fábrica e por quê?
features_c = ["estado_vendedor", "garantia_de_fábrica"]
search_c = df[features_c].dropna(axis=0)
list_c = (
    search_c.groupby("estado_vendedor")
    .count()
    .sort_values(by=["garantia_de_fábrica"], ascending=False)
)
# print(list_c.head())
