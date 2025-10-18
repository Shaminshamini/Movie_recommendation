import matplotlib.pyplot as plt
import seaborn as sns

def plot_genre_trends(df):
    genre_avg = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    sns.barplot(x=genre_avg.values, y=genre_avg.index)
    plt.title('Average Ratings by Genre')
    plt.xlabel('Average Rating')
    plt.ylabel('Genre')
    plt.show()
