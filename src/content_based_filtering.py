from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compute_cosine_similarity(movies_df, genre_columns):
    movies_df['genres_str'] = movies_df[genre_columns].apply(lambda x: ' '.join(x.index[x == 1]), axis=1)
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(movies_df['genres_str'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return movies_df, cosine_sim

def get_similar_movies(title, movies_df, cosine_sim, top_n=5):
    idx = movies_df[movies_df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:top_n+1]]
    return movies_df.iloc[movie_indices][['title']]
