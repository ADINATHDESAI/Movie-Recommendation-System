import streamlit as st  # Import Streamlit for UI components
import pickle           # Import pickle for loading saved models/data
import pandas as pd     # Import pandas for DataFrame manipulation
import requests         # Import requests to make API calls
import os
import gdown

# Set up the Streamlit page configuration with title and icon
st.set_page_config(page_title="Adinath's Movie Recommendation System Project" , page_icon='🎥')

st.sidebar.markdown("""
# Project By: ADINATH DESAI

**Email:** [adinath.desai04@gmail.com](mailto:adinath.desai04@gmail.com)  
**LinkedIn:** [Adinath Desai](https://www.linkedin.com/in/adinath-desai-1b533a260)
""")

st.title('Movie Recommendation System')  # Set the title of the app

st.markdown("""
    <div style="border: 2px solid; padding: 10px; background-color: #f0f0f0; color: #000000; border-color: #d1d1d1;">
        Welcome! This project demonstrates a movie recommendation system using machine learning. Feel free to explore the recommendations below.
    </div>
""", unsafe_allow_html=True)

# Add a dark mode fallback by using a more fitting style for dark mode
st.markdown("""
    <style>
        .streamlit-expanderHeader {
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# Function to fetch the poster image URL for a given movie_id using TMDB API
def fetch_poster(movie_id):
    # Construct the URL with the movie_id and API key
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    # Get the JSON response from the API
    data = requests.get(url)
    data = data.json()
    # Extract the poster path from the JSON data
    poster_path = data['poster_path']
    # Create the full URL for the poster image
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# -------------------------------
# Helper Function to Download Files
# -------------------------------
def download_file(url, filename):
    """Download a file from a URL if it doesn't exist locally."""
    if not os.path.exists(filename):
        with st.spinner("Please wait while we set things up for you."):
            gdown.download(url=url, output=filename, quiet=False)
    else:
        pass

# URLs for your files hosted externally (replace with your actual URLs)
SIMILARITY_URL = "https://drive.google.com/uc?export=download&id=1n-YuwfbEKw9_Mp1d5UOs1njhMPz-EOYU"
MOVIES_DICT_URL = "https://drive.google.com/uc?export=download&id=1YalorKo6_2HJsDOsEOurjHmXFRsOslXo"

# Local filenames
SIMILARITY_FILE = "similarity.pkl"
MOVIES_DICT_FILE = "movies_dict.pkl"

# -------------------------------
# Download the files only once at app startup
# -------------------------------
download_file(SIMILARITY_URL, SIMILARITY_FILE)
download_file(MOVIES_DICT_URL, MOVIES_DICT_FILE)

# Function to recommend movies based on a selected movie title
def recommend(movie):
    # Get the index of the movie from the movies DataFrame
    movies_index = movies[movies['title']==movie].index[0]
    # Retrieve the similarity scores for the selected movie
    distances = similarity[movies_index]
    # Sort the movies based on similarity scores and get the top 5 recommendations (excluding the selected movie)
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_poster = []  # List to store poster URLs for recommended movies
    recommended_movies = []         # List to store recommended movie titles

    # Iterate through the top similar movies
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id    # Get the movie id for fetching the poster
        recommended_movies.append(movies.iloc[i[0]].title) # Append the movie title to the recommendations list
        # Fetch poster using the API and append to the poster list 
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_poster

# Load the movies dictionary from the pickle file and convert it to a DataFrame
movies_dict = pickle.load(open(MOVIES_DICT_FILE, 'rb'))
movies = pd.DataFrame(movies_dict)
# Load the similarity matrix from the pickle file
similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))


# Create a select box widget for the user to select a movie from the DataFrame titles
selected_movie_name = st.selectbox("Select the Movie Name", movies['title'].values)

# When the button is clicked, display movie recommendations
if st.button("🎬 Show Movie Recommendations"):
    # Get the recommended movie names and their corresponding poster URLs using the recommend function
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    # Create five columns for displaying the recommended movies
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display each recommended movie's poster and title in separate columns
    for col, name, poster in zip([col1, col2, col3, col4, col5], recommended_movie_names, recommended_movie_posters):
        with col:
            st.image(poster, use_container_width=True)  # Updated: use_container_width replaces use_column_width
            st.markdown(f"**🎥 {name}**", unsafe_allow_html=True)  # Bold movie title with emoji














###########################################################################################3
# import os
# import streamlit as st  # Import Streamlit for UI components
# import pickle           # Import pickle for loading saved models/data
# import pandas as pd     # Import pandas for DataFrame manipulation
# import requests         # Import requests to make API calls

# # -------------------------------
# # Helper Function to Download Files
# # -------------------------------
# def download_file(url, filename):
#     """Download a file from a URL if it doesn't exist locally."""
#     if not os.path.exists(filename):
#         r = requests.get(url, stream=True)
#         r.raise_for_status()  # Raise an error if the download fails
#         with open(filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#         st.info(f"Downloaded {filename}")
#     else:
#         st.info(f"{filename} already exists.")

# # URLs for your files hosted externally (replace with your actual URLs)
# SIMILARITY_URL = "https://drive.google.com/uc?export=download&id=1n-YuwfbEKw9_Mp1d5UOs1njhMPz-EOYU"
# MOVIES_DICT_URL = "https://drive.google.com/uc?export=download&id=1YalorKo6_2HJsDOsEOurjHmXFRsOslXo"

# # Local filenames
# SIMILARITY_FILE = "similarity.pkl"
# MOVIES_DICT_FILE = "movies_dict.pkl"

# # -------------------------------
# # Download the files only once at app startup
# # -------------------------------
# download_file(SIMILARITY_URL, SIMILARITY_FILE)
# download_file(MOVIES_DICT_URL, MOVIES_DICT_FILE)

# # -------------------------------
# # Load the required files
# # -------------------------------
# movies_dict = pickle.load(open(MOVIES_DICT_FILE, 'rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))

# # -------------------------------
# # Define helper functions for the app
# # -------------------------------
# def fetch_poster(movie_id):
#     """Fetch the poster image URL for a given movie_id using TMDB API."""
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url).json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def recommend(movie):
#     """Recommend movies based on the selected movie title."""
#     movies_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movies_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

#     recommended_movies_poster = []  # Store poster URLs
#     recommended_movies = []         # Store movie titles

#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_poster.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_poster

# # -------------------------------
# # Streamlit App Configuration and UI
# # -------------------------------
# st.set_page_config(page_title="Adinath's Movie Recommendation System Project", page_icon='🎥')

# st.sidebar.markdown("""
# # Project By: ADINATH DESAI

# **Email:** [adinath.desai04@gmail.com](mailto:adinath.desai04@gmail.com)  
# **LinkedIn:** [Adinath Desai](https://www.linkedin.com/in/adinath-desai-1b533a260)
# """)

# st.title('Movie Recommendation System')
# st.markdown("""
#     <div style="border: 2px solid; padding: 10px; background-color: #f0f0f0; color: #000000; border-color: #d1d1d1;">
#         Welcome! This project demonstrates a movie recommendation system using machine learning. Feel free to explore the recommendations below.
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#         .streamlit-expanderHeader {
#             background-color: transparent !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

# selected_movie_name = st.selectbox("Select the Movie Name", movies['title'].values)

# if st.button("🎬 Show Movie Recommendations"):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)

#     for col, name, poster in zip([col1, col2, col3, col4, col5], recommended_movie_names, recommended_movie_posters):
#         with col:
#             st.image(poster, use_container_width=True)
#             st.markdown(f"**🎥 {name}**", unsafe_allow_html=True)
