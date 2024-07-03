import pandas as pd
import numpy as np
import ast

def read_csv_file(file_path: str) -> pd.DataFrame:
    """Read a CSV file and return a DataFrame."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"Error: {e}")
        return pd.DataFrame()

def merge_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, key: str) -> pd.DataFrame:
    """Merge two DataFrames on a key."""
    try:
        return df1.merge(df2, on=key)
    except KeyError as e:
        print(f"Error: {e}")
        return pd.DataFrame()

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the DataFrame by selecting relevant columns, removing null values, and duplicates."""
    df = df[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']].copy()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

# Define main function to orchestrate the dataset creation
def main():
    movies_df = read_csv_file('./data/raw/tmdb_5000_movies.csv')
    credits_df = read_csv_file('./data/raw/tmdb_5000_credits.csv')

    if not movies_df.empty and not credits_df.empty:
        movies_df = merge_dataframes(movies_df, credits_df, 'title')
        movies_df = preprocess_data(movies_df)
        movies_df.to_csv('./data/interim/movies_preprocessed.csv', index=False)

if __name__ == "__main__":
    main()