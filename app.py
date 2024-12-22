import pandas as pd
import pickle
import streamlit as st

# Load Precomputed Models


@st.cache_resource
def load_pkl(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Load Dataset


@st.cache_data
def load_data(file_path="spotify_songs.csv"):
    return pd.read_csv(file_path)

# Content-Based Recommendations


def content_based_recommendations(df, content_similarity, song_name, top_n=10):
    try:
        song_index = df[df['track_name'].str.contains(
            song_name, case=False, na=False)].index[0]
    except IndexError:
        st.error(f"Song '{song_name}' not found in the dataset.")
        return pd.DataFrame()
    similar_songs = content_similarity[song_index]
    song_indices = similar_songs.argsort()[-top_n:][::-1]
    return df.iloc[song_indices][['track_name', 'track_artist']]

# Hybrid Recommendations


def hybrid_recommendations(df, features, song_name, collab_recs, content_similarity, top_n=10):
    content_recs = content_based_recommendations(
        df, content_similarity, song_name, top_n)
    if content_recs.empty:
        return pd.DataFrame()

    song_id = df[df['track_name'].str.contains(
        song_name, case=False, na=False)]['track_id'].values[0]
    collab_song_ids = collab_recs.get(song_id, [])
    collab_recs_df = df[df['track_id'].isin(collab_song_ids)][[
        'track_name', 'track_artist']]

    combined = pd.concat([content_recs, collab_recs_df]).drop_duplicates()
    return combined.head(top_n)

# Streamlit App


def app():
    st.title("Optimized Hybrid Music Recommendation System")

    # Load Precomputed Models and Data
    df = load_data()
    content_similarity = load_pkl("content_similarity.pkl")
    collab_recs = load_pkl("collaborative_recommendations.pkl")

    st.subheader("Search for a Song")
    song_name = st.text_input("Enter song name")

    if st.button("Get Recommendations"):
        if not song_name:
            st.error("Please enter a song name to get recommendations.")
            return

        recs = hybrid_recommendations(
            df, None, song_name, collab_recs, content_similarity)
        if not recs.empty:
            st.write("Here are your recommendations:")
            st.write(recs)
        else:
            st.write("No recommendations found.")


if __name__ == "__main__":
    app()
