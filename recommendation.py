import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import pickle

# Load Dataset


def load_data(file_path="spotify_songs.csv"):
    return pd.read_csv(file_path)

# Preprocessing


def preprocess_data(df):
    features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
                'instrumentalness', 'liveness', 'valence', 'tempo']
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])
    return df, features

# Precompute Collaborative Recommendations


def precompute_collaborative(df, top_n=10):
    pivot_table = pd.pivot_table(
        df, values='track_popularity', index='track_id', columns='playlist_id').fillna(0)
    sparse_matrix = csr_matrix(pivot_table.values)

    model = TruncatedSVD(n_components=50, random_state=42)
    latent_matrix = model.fit_transform(sparse_matrix)
    similarity_matrix = cosine_similarity(latent_matrix)

    recommendations = {}
    for idx, song_id in enumerate(pivot_table.index):
        similar_indices = similarity_matrix[idx].argsort()[-top_n-1:-1][::-1]
        similar_songs = pivot_table.index[similar_indices].tolist()
        recommendations[song_id] = similar_songs
    return recommendations

# Save Precomputed Data


def save_to_pkl(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


if __name__ == "__main__":
    df = load_data()
    df, features = preprocess_data(df)

    # Precompute collaborative recommendations
    collab_recs = precompute_collaborative(df)
    save_to_pkl(collab_recs, "collaborative_recommendations.pkl")

    # Precompute content similarity matrix
    content_similarity = cosine_similarity(df[features])
    save_to_pkl(content_similarity, "content_similarity.pkl")
