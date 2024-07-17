import pandas as pd
import pickle

# Carregar o modelo salvo
with open('modelo.pkl', 'rb') as file:
    model = pickle.load(file)

# Dados do novo filme
new_movie = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': "1994",
    'Certificate': 'A',
    'Runtime': "142 min",
    'Genre': 'Drama',
    'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': 28341469  # Convertido para valor numérico
}

# Converter para DataFrame
new_movie_df = pd.DataFrame([new_movie])

# Transformar dados usando o pré-processador
try:
    X_new = new_movie_df.drop(columns=['Series_Title', 'Overview'])
    X_new_transformed = model.named_steps['preprocessor'].transform(X_new)
    # Fazer previsão
    y_new_pred = model.named_steps['regressor'].predict(X_new_transformed)
    print(f'Predicted IMDb rating for {new_movie["Series_Title"]}: {y_new_pred[0]}')
except Exception as e:
    print(f'Error during prediction: {e}')
