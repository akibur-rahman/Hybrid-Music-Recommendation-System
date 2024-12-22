🎵 Hybrid Music Recommendation System
A Hybrid Music Recommendation System that combines Collaborative Filtering and Content-Based Filtering to provide personalized song recommendations. This system leverages audio features (e.g., danceability, energy) and user interactions (e.g., playlists) to recommend songs quickly and efficiently.

🚀 Features
Hybrid Approach: Combines collaborative and content-based recommendations.
Precomputed Models: Saves recommendations and similarity matrices for faster runtime performance.
Interactive UI: Built with Streamlit for user-friendly interaction.
Scalable Design: Handles large datasets using sparse matrices and dimensionality reduction techniques.
📂 Dataset
The system uses the Spotify 30k Songs Dataset, which includes:

Song metadata: track_name, track_artist, track_popularity.
Audio features: danceability, energy, tempo, etc.
Playlist data: playlist_name, playlist_genre, playlist_id.
Ensure the dataset is saved as spotify_songs.csv in the project directory.

⚙️ Tech Stack
Python: Core programming language.
pandas: Data manipulation and preprocessing.
scikit-learn: Similarity calculations, scaling, and dimensionality reduction.
scipy: Efficient handling of sparse matrices.
pickle: Precomputing and saving models.
Streamlit: Frontend for user interaction.
🛠️ Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/hybrid-music-recommendation-system.git
cd hybrid-music-recommendation-system
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Place the dataset in the project directory:

bash
Copy code
spotify_songs.csv
🏗️ Project Structure
plaintext
Copy code
.
├── app.py                  # Streamlit app
├── precompute.py           # Precomputes recommendations
├── spotify_songs.csv       # Dataset (30k Spotify songs)
├── collaborative_recommendations.pkl # Precomputed collaborative recommendations
├── content_similarity.pkl  # Precomputed content similarity matrix
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
📖 How It Works
1. Precompute Recommendations
Run precompute.py to generate precomputed models for collaborative and content-based filtering:

bash
Copy code
python precompute.py
This script performs the following steps:

Loads the dataset.
Normalizes audio features using MinMaxScaler.
Precomputes:
Collaborative Recommendations: Using Truncated SVD and cosine similarity.
Content Similarity Matrix: Using audio features.
The results are saved in .pkl files for faster runtime access.

2. Run the Streamlit App
Launch the interactive frontend:

bash
Copy code
streamlit run app.py
Features of the app:

Input Preferences: Users can specify song preferences or playlist genres.
Real-Time Recommendations: Combines collaborative and content-based methods to suggest songs.
🧠 Theory
Hybrid Recommendation System
Collaborative Filtering:
Uses user-item interactions (songs in playlists) to find similar songs.
Employs Truncated SVD to reduce matrix dimensionality and improve computational efficiency.
Content-Based Filtering:
Utilizes audio features (e.g., danceability, tempo) to find songs with similar characteristics.
Computes pairwise similarity using cosine similarity.
Precomputations
To optimize for speed:

Collaborative recommendations and content similarity matrices are computed offline.
Precomputed data is stored in .pkl files and loaded during runtime for instant access.
🛠️ Customization
Modify the Dataset
Replace spotify_songs.csv with a different dataset, ensuring it contains:

Audio features for content-based filtering.
User-item interaction data for collaborative filtering.
Adjust Recommendation Logic
Change the number of similar songs (top_n) in precompute_collaborative.
Use additional audio features in preprocess_data.
📈 Performance Optimization
Sparse Matrices: Efficiently handles large user-item matrices with csr_matrix.
Precomputations: Reduces runtime computations for real-time recommendations.
Dimensionality Reduction: Improves similarity calculations using latent features from Truncated SVD.
🧪 Example Usage
Precompute Recommendations:

bash
Copy code
python precompute.py
Run the App:

bash
Copy code
streamlit run app.py
Interact with the UI:

Select a genre, playlist, or audio feature preferences.
Get real-time song recommendations.
📜 License
This project is open-source and available under the MIT License.

👥 Contributors
Your Name (Project Lead)
Collaborators
Feel free to contribute! 🎉

💬 Feedback
If you have suggestions or issues, feel free to open an issue or reach out. 🚀