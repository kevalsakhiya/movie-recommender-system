import os
import joblib
import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv



def fetch_movie_poster(movie_id: int) -> str:
    """
    Fetch the poster URL for a given movie ID.

    Args:
        movie_id (int): The ID of the movie.

    Returns:
        str: The full URL to the movie poster.
    """
    load_dotenv()
    api_key = os.getenv('tmdb_api_key')
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if not poster_path:
            raise ValueError(f"No poster path found for movie ID: {movie_id}")
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except requests.RequestException as e:
        st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
        return ""
    except ValueError as e:
        st.error(e)
        return ""


def recommend_movies(movie_title: str) -> tuple[list[str], list[str]]:
    """
    Recommend movies based on a given movie title.

    Args:
        movie_title (str): The title of the movie.

    Returns:
        tuple: A tuple containing a list of recommended movie names and their corresponding poster URLs.
    """
    try:
        index = movies[movies['title'] == movie_title].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_movie_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters
    except IndexError:
        st.error(f"Movie '{movie_title}' not found in the database.")
        return [], []
    except Exception as e:
        st.error(f"Error recommending movies: {e}")
        return [], []


def load_data():
    """
    Load the movies data and similarity matrix.

    Returns:
        tuple: A tuple containing the movies DataFrame and similarity matrix.
    """
    try:
        movies_dict = joblib.load(open('models/movie_model.joblib', 'rb'))
        similarity_matrix = joblib.load(open('models/movie_model_similarity.joblib', 'rb'))
        movies_df = pd.DataFrame(movies_dict)
        return movies_df, similarity_matrix
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(), None


def display_recommendations(movie_names: list[str], movie_posters: list[str]) -> None:
    """
    Display the recommended movies and their posters.

    Args:
        movie_names (list[str]): List of recommended movie names.
        movie_posters (list[str]): List of URLs to the recommended movie posters.
    """
    if movie_names and movie_posters:
        cols = st.columns(5)
        for col, name, poster in zip(cols, movie_names, movie_posters):
            with col:
                st.text(name)
                st.image(poster)


# Main application
st.header('Movie Recommender System')

movies, similarity = load_data()

if not movies.empty:
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend_movies(selected_movie)
        display_recommendations(recommended_movie_names, recommended_movie_posters)
else:
    st.error("No movie data available.")
