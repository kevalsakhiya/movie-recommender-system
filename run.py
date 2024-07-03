# Example command - python run_project.py "Avatar"

import subprocess

def run_data_preprocessing():
    """Run data preprocessing script."""
    subprocess.run(["python", "src/data/make_dataset.py"], check=True)

def run_feature_engineering():
    """Run feature engineering script."""
    subprocess.run(["python", "src/features/build_features.py"], check=True)

def run_model_training():
    """Run model training script."""
    subprocess.run(["python", "src/models/train_model.py"], check=True)

def run_movie_recommendation(movie_title: str):
    """Run movie recommendation script."""
    subprocess.run(["python", "src/models/predict_model.py", movie_title], check=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        movie_title = sys.argv[1]
        try:
            print("Running data preprocessing...")
            run_data_preprocessing()
            
            print("Running feature engineering...")
            run_feature_engineering()
            
            print("Running model training...")
            run_model_training()
            
            print(f"Getting recommendations for movie: {movie_title}...")
            run_movie_recommendation(movie_title)
            
            print("Project run successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    else:
        print("Please provide a movie title as an argument.")
