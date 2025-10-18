import pandas as pd

def find_similar_movies(matrix, target_movie):
    target_ratings = matrix[target_movie]
    similarity = matrix.corrwith(target_ratings)
    
    corr_df = pd.DataFrame(similarity, columns=['Correlation'])
    corr_df.dropna(inplace=True)
    corr_df = corr_df.sort_values('Correlation', ascending=False)
    return corr_df
