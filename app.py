import streamlit
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=649515a4af9648690ce810524e3d84c7&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def release_date(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=649515a4af9648690ce810524e3d84c7&language=en-US'.format(movie_id))
    data = response.json()
    return data['release_date']


def overview(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=649515a4af9648690ce810524e3d84c7&language=en-US'.format(movie_id))
    data = response.json()
    return data['overview']

def adult(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=649515a4af9648690ce810524e3d84c7&language=en-US'.format(movie_id))
    data = response.json()
    return data['adult']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_release = []
    recommended_movies_overview = []
    recommended_movies_adult = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching_movies_posters
        recommended_movies_poster.append(fetch_poster(movie_id))
        # fetching release data
        recommended_movies_release.append(release_date(movie_id))
        # fetching overview
        recommended_movies_overview.append(overview(movie_id))
        # fetching adult
        recommended_movies_adult.append(adult(movie_id))

    return recommended_movies, recommended_movies_poster, recommended_movies_release, recommended_movies_overview, recommended_movies_adult

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
# Include Animate.css in the Streamlit app
streamlit.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

streamlit.markdown("""
        <h1 style="color : red;"class="animate__animated animate__zoomIn"> Movie Recommender System </h1>
""", unsafe_allow_html=True)
selected_movie_name = streamlit.selectbox(
    'Select a movie that you like ',
    movies['title'].values
)

if streamlit.button('Recommend'):
    names, posters, date, overview, adult= recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = streamlit.columns(5)
    with col1:
        streamlit.text("Adult rating:" + str(adult[0]))
        streamlit.text(names[0])
        streamlit.image(posters[0])
        streamlit.text(date[0])
        streamlit.write(overview[0])  
    with col2:
        streamlit.text("Adult rating:" + str(adult[1]))
        streamlit.text(names[1])
        streamlit.image(posters[1])
        streamlit.text(date[1])
        streamlit.write(overview[1])
    with col3:
        streamlit.text("Adult rating:" + str(adult[2]))
        streamlit.text(names[2])
        streamlit.image(posters[2])
        streamlit.text(date[2])
        streamlit.write(overview[2])
    with col4:
        streamlit.text("Adult rating:" + str(adult[3]))
        streamlit.text(names[3])
        streamlit.image(posters[3])
        streamlit.text(date[3])
        streamlit.write(overview[3])
    with col5:
        streamlit.text("Adult rating:" + str(adult[4]))
        streamlit.text(names[4])
        streamlit.image(posters[4])
        streamlit.text(date[4])
        streamlit.write(overview[4])




