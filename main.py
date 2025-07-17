#Import Libraries and Load the Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')

# Define column names
columns = ['user_id', 'movie_id', 'rating', 'timestamp']

# Load ratings data
ratings_df = pd.read_csv('file.tsv', sep='\t', names=columns)

# Load movie title mapping
movies_df = pd.read_csv('Movie_Id_Titles.csv')
movies_df.columns = ['movie_id', 'title']

# Merge movie titles with ratings
merged_df = pd.merge(ratings_df, movies_df, on='movie_id')
