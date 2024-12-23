
# 🎵 Hybrid Music Recommendation System
This project is a Hybrid Music Recommendation System that combines Collaborative Filtering and Content-Based Filtering to recommend songs based on user preferences and song features. It uses a dataset of Spotify songs and provides fast, real-time recommendations via a Streamlit user interface.

## 🚀 Features

- Hybrid Recommendations: Combines collaborative filtering (user interaction-based) and content-based filtering (song feature-based).
- Precomputed Data: Saves precomputed similarity matrices and recommendations for fast predictions.
- Streamlit UI: A user-friendly interface for personalized song recommendations.


## 🧠 How It Works
1. Collaborative Filtering:
- Based on user-song interactions (e.g., playlists).
- Uses a user-item matrix to calculate similarity between songs by analyzing co-occurrence in playlists.
- Truncated SVD reduces dimensionality and captures latent features.
- Cosine similarity is used to measure how similar songs are in the latent feature space.
2. Content-Based Filtering:
- Based on song features such as danceability, energy, loudness, etc.
- These features are normalized using MinMaxScaler.
- Cosine similarity is then used to find songs that share similar audio features.
3. Hybrid Model:
- The system combines both collaborative and content-based recommendations to provide personalized suggestions based on real user inputs and song features.
4. Precomputations:
- Recommendations and similarity matrices are computed offline to ensure fast real-time access during user interaction.
- Pickle is used to save and load precomputed data for quick access.

## 📂 Dataset
The system uses the Spotify 30k Songs Dataset from kaggle that contains:
- Song metadata: `track_name`, `track_artist`, `track_popularity`.
- Audio features: `danceability`, `energy`, `tempo`, etc.
- Playlist data: `playlist_name`, `playlist_genre`, `playlist_id`.
- Ensure that the dataset is saved as spotify_songs.csv in the project directory.
## 🛠️ Installation
1. Clone the repository:
```git clone https://github.com/akibur-rahman/Hybrid-Music-Recommendation-System.git```


## 📜 License

This project is open-source and available under the [MIT](https://choosealicense.com/licenses/mit/)


## 👥 Contributors
- Akibur Rahman
- Afique Hossain