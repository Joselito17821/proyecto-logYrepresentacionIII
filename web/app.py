# file: 'web/app.py'
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, render_template
import pandas as pd
from src.preprocessing import filter_data
from src.collaborative_filtering import train_svd_model
from src.topn_recommendation import get_top_n

app = Flask(__name__)

# Carga los ratings y metadatos de películas
ratings = pd.read_csv("../data/ratings.csv")
movies_df = pd.read_csv("../data/movies.csv")
movie_id_to_title = dict(zip(movies_df["movieId"], movies_df["title"]))

# Filtra los datos para acelerar el entrenamiento
filtered_ratings = filter_data(ratings, min_user_ratings=20, min_movie_ratings=50)

# Entrena el modelo con datos filtrados y calcula Top-N
model, predictions = train_svd_model(filtered_ratings)
top_n = get_top_n(predictions, n=5)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_id = request.form.get("userId", "").strip()
    try:
        user_id = int(user_id)
        recommendations = top_n.get(user_id, [])
        recommendations_with_titles = [
            {"movieTitle": movie_id_to_title.get(movie_id, f"Movie {movie_id}"), "score": round(score, 2)}
            for movie_id, score in recommendations
        ]
        return render_template("results.html", recommendations=recommendations_with_titles)
    except Exception as e:
        return render_template("results.html", recommendations=[], error=str(e))

@app.route("/api/recommend", methods=["GET"])
def api_recommend():
    try:
        user_id = int(request.args.get("userId", "").strip())
    except Exception:
        return jsonify(recommendations=[], error="userId inválido"), 400

    recommendations = top_n.get(user_id, [])
    return jsonify(recommendations=[
        {
            "movieTitle": movie_id_to_title.get(mid, f"Movie ID {mid} (Title Not Found)"),
            "score": round(score, 2)
        }
        for mid, score in recommendations
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)