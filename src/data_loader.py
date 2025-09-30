import pandas as pd

def load_movielens_data(filepath: str) -> pd.DataFrame:
    """
    Loads the MovieLens dataset CSV.
    """
    return pd.read_csv(filepath)
