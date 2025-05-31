import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ✅ Your Dropbox links
SIMILARITY_URL = "https://www.dropbox.com/scl/fi/wj7fr9krcpj2zqvhh9xyj/similarity.pkl?rlkey=qj2wbgjvkech68zf67pzqvr1i&st=30496nf1&dl=1"
MOVIE_DICT_URL = "https://www.dropbox.com/scl/fi/3sq5i3vb5h4hzsahlr76b/movie_dict.pkl?rlkey=5b644f4qv69hbo0jepma4mkux&st=optoaexm&dl=1"

# ✅ Function to download files from external link
def download_file_from_url(url, filename):
    if not os.path.exists(filename):
        st.info(f'Downloading {filename}...')
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        st.success(f'{filename} downloaded successfully.')

# ✅ Download the files
download_file_from_url(SIMILARITY_URL, "similarity.pkl")
download_file_from_url(MOVIE_DICT_URL, "movie_dict.pkl")

# ✅ Load the data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ✅ TMDB API: fetch poster
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=395261f65e50e040d1e6cab88485df2c&language=en-US'
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# ✅ Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ✅ Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
