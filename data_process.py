def create_user_movie_matrix(df):
    matrix = df.pivot_table(index='user_id', columns='title', values='rating')
    return matrix
