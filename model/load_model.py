import pandas as pd
import pickle


with open('model/modelo.pkl', 'rb') as file:
    data = pickle.load(file)

model = data['model']
label_enc = data['label_enc']
one_hot_enc = data['one_hot_enc']

new_house = {
 'id': 2595,
 'nome': 'Skylit Midtown Castle',
 'host_id': 2845,
 'host_name': 'Jennifer',
 'bairro_group': 'Manhattan',
 'bairro': 'Midtown',
 'latitude': 40.75362,
 'longitude': -73.98377,
 'room_type': 'Entire home/apt',
 'minimo_noites': 1,
 'numero_de_reviews': 45,
 'ultima_review': '2019-05-21',
 'reviews_por_mes': 0.38,
 'calculado_host_listings_count': 2,
 'disponibilidade_365': 355
}

new_house_df = pd.DataFrame([new_house])

try:
    features = ['id', 'bairro_group', 'bairro', 'latitude', 'longitude', 'room_type', 'minimo_noites', 'numero_de_reviews', 'reviews_por_mes', 'disponibilidade_365']
    X_house = new_house_df[features]

    X_house['bairro'] = label_enc.transform(X_house['bairro'])
    X_encoded = one_hot_enc.transform(X_house[['bairro_group', 'room_type']])

    X_encoded_df = pd.DataFrame(X_encoded, columns=one_hot_enc.get_feature_names_out(['bairro_group', 'room_type']))
    X_encoded_df.index = X_house.index
    X_house_transformed = pd.concat([X_house, X_encoded_df], axis=1).drop(columns=['bairro_group', 'room_type'])

    y_new_pred = model.predict(X_house_transformed)
    print(f'O valor estimado para aluguel do imóvel é de R${y_new_pred[0]:.2f}')
except Exception as e:
    print(f'Error during prediction: {e}')