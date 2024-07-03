# Movie Recommender System
==============================

Welcome to the Movie Recommender System project! This project utilizes the popular TMDB_5000 dataset from Kaggle to create a content-based movie recommendation system. The system uses genres, directors, actors, and descriptions to generate recommendations based on content similarity.

## Features

- **Data Preprocessing**: Cleans and preprocesses movie data.
- **Feature Engineering**: Creates tags based on genres, directors, actors, and descriptions.
- **Vectorization**: Uses NLTK's Bag of Words to vectorize the tags.
- **Content Similarity**: Measures content similarity using cosine similarity.
- **Streamlit App**: Provides an interactive interface to get movie recommendations.
- **Run Script**: Includes a `run.py` file to run the entire project workflow in one go.

## Dataset

The project uses the TMDB 5000 Movies Dataset from Kaggle. You can find the dataset [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

## Requirements

To install the necessary dependencies, run:

```sh
pip install -r requirements.txt
```

Project Organization
------------


    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- The processed dataset.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
