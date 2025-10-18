from database_connect import load_data
from data_process import create_user_movie_matrix
from collaborate import find_similar_movies
from visualization import plot_genre_trends

def main():
    print("🎬 Loading data...")
    df = load_data()

    print("📊 Preparing user-movie matrix...")
    matrix = create_user_movie_matrix(df)

    print("🎯 Finding similar movies to 'Inception'...")
    corr_df = find_similar_movies(matrix, 'Inception')
    print(corr_df.head())

    print("📈 Plotting genre trends...")
    plot_genre_trends(df)

if __name__ == "__main__":
    main()
