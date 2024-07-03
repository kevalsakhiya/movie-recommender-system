from nltk.stem.porter import PorterStemmer
import pandas as pd
import ast

def convert(obj: str) -> list:
    """Convert a JSON-like string to a list of genre/keyword names."""
    try:
        return [i['name'] for i in ast.literal_eval(obj)]
    except (ValueError, SyntaxError) as e:
        print(f"Error: {e}")
        return []

def convert_top_n(obj: str, n: int = 3) -> list:
    """Convert a JSON-like string to a list of top N names."""
    try:
        return [i['name'] for i in ast.literal_eval(obj)[:n]]
    except (ValueError, SyntaxError) as e:
        print(f"Error: {e}")
        return []

def fetch_director(obj: str) -> list:
    """Fetch the director's name from the crew column."""
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return [i['name']]
        return []
    except (ValueError, SyntaxError) as e:
        print(f"Error: {e}")
        return []

def preprocess_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Apply preprocessing functions to relevant columns."""
    df['genres'] = df['genres'].apply(convert)
    df['keywords'] = df['keywords'].apply(convert)
    df['cast'] = df['cast'].apply(convert_top_n)
    df['crew'] = df['crew'].apply(fetch_director)
    df['overview'] = df['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])
    return df

def remove_spaces(df: pd.DataFrame) -> pd.DataFrame:
    """Remove spaces from the strings in the columns."""
    for column in ['genres', 'keywords', 'cast', 'crew']:
        df[column] = df[column].apply(lambda x: [i.replace(' ', '') for i in x])
    return df

def create_tags_column(df: pd.DataFrame) -> pd.DataFrame:
    """Create a new 'tags' column by concatenating relevant columns."""
    df['tags'] = df['overview'] + df['genres'] + df['keywords'] + df['cast'] + df['crew']
    return df

def join_tags(df: pd.DataFrame) -> pd.DataFrame:
    """Join the tags list into a single string and convert to lowercase."""
    df['tags'] = df['tags'].apply(lambda x: ' '.join(x).lower())
    return df

def stem_text(text: str, ps: PorterStemmer) -> str:
    """Stem the words in the text."""
    return " ".join([ps.stem(word) for word in text.split()])

def stem_tags(df: pd.DataFrame, ps: PorterStemmer) -> pd.DataFrame:
    """Apply stemming to the tags column."""
    df['tags'] = df['tags'].apply(lambda x: stem_text(x, ps))
    return df

# Define main function to orchestrate the feature building
def main():
    movies_df = pd.read_csv('./data/interim/movies_preprocessed.csv')
    movies_df = preprocess_columns(movies_df)
    movies_df = remove_spaces(movies_df)
    movies_df = create_tags_column(movies_df)
    movies_df = join_tags(movies_df)

    ps = PorterStemmer()
    movies_df = stem_tags(movies_df, ps)

    movies_df.to_csv('./data/processed/movies_features.csv', index=False)

if __name__ == "__main__":
    main()
