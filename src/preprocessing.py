import pandas as pd

def filter_data(df: pd.DataFrame, min_user_ratings=50, min_movie_ratings=100):
    """
    Filters users and movies based on minimum ratings.
    """
    user_counts = df['userId'].value_counts()
    movie_counts = df['movieId'].value_counts()

    df = df[df['userId'].isin(user_counts[user_counts >= min_user_ratings].index)]
    df = df[df['movieId'].isin(movie_counts[movie_counts >= min_movie_ratings].index)]
    return df

def create_user_item_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a user-item rating matrix.
    """
    return df.pivot_table(index='userId', columns='movieId', values='rating')
