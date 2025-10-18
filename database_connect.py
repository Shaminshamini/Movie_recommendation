import pandas as pd

def load_data():
    movies = pd.read_csv("../data/movies.csv")
    ratings = pd.read_csv("../data/ratings.csv")
    users = pd.read_csv("../data/users.csv")
    
    df = pd.merge(ratings, movies, on="movie_id")
    return df

