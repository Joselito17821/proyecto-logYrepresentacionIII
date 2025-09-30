from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

def train_svd_model(df):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    predictions = model.test(testset)
    return model, predictions
