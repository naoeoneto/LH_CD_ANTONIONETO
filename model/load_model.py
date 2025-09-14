import os, pickle
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "modelo.pkl")

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

new_movie = {
    'Series_Title':'The Shawshank Redemption',
    'Released_Year':"1994",
    'Certificate':'A',
    'Runtime':"142 min",
    'Genre':'Drama',
    'Overview':'Two imprisoned men...',
    'Meta_score':80.0,
    'Director':'Frank Darabont',
    'Star1':'Tim Robbins',
    'Star2':'Morgan Freeman',
    'Star3':'Bob Gunton',
    'Star4':'William Sadler',
    'No_of_Votes':2343110,
    'Gross':28341469
}
df_new = pd.DataFrame([new_movie])
X_new = df_new.drop(columns=['Series_Title','Overview'], errors='ignore')

y_new = model.predict(X_new)[0]
print(f"Predicted IMDb rating for {new_movie['Series_Title']}: {y_new:.4f}")
