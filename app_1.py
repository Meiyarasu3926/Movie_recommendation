import streamlit as st
import pickle
import pandas as pd
import difflib
import requests
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


model = pickle.load(open('movie_df.pkl', 'rb'))

st.title("Movie Recommendation System")

df = pd.DataFrame(model)

vector = CountVectorizer(max_features=5000, stop_words='english', lowercase=True)
cv = vector.fit_transform(df['tag'])

cosine = cosine_similarity(cv)

input_box = st.selectbox("Enter your favorite movie: ", df['title'].values)


def fetch_poster(movie_id):
	url = "https://api.themoviedb.org/3/movie/{}?api_key=049c031f3b29bdb8727c647bd4b2041f&language=en-US".format(movie_id)
	
	response = requests.get(url)
	data = response.json()
	
	poster_path = data['poster_path']
	
	return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
	movie_lst = []
	movie_poster = []
	title_lst = df['title'].to_list()
	close_match = difflib.get_close_matches(movie, title_lst)[0]
	movie_index = df[df['title'] == close_match].index[0]
	distance = cosine[movie_index] 
    	
	movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[:13]
    	
	for i, v in movie_list:
		movie_id = df.iloc[i]['movie_id']
		movie_lst.append(df.iloc[i]['title'])
		movie_poster.append(fetch_poster(movie_id))
        
	return movie_lst, movie_poster
	
if st.button("View Suggestions"):
	name, poster = recommend(input_box)
	
	col1, col2 = st.columns(2)
	with col1:
		st.image(poster[0])
		st.write(name[0])

	st.markdown("<h3 style='font-size:40px; color:white;'>This is for you:</h3>", unsafe_allow_html=True)	
	col1, col2, col3, col4 = st.columns(4)
	
	
	
	
	with col1:
		st.image(poster[1])
		st.write(name[1])
		
	with col2:
		st.image(poster[2])
		st.write(name[2])
		
	with col3:
		st.image(poster[3])
		st.write(name[3])
		
	with col4:
		st.image(poster[4])
		st.write(name[4])
		
	with col1:
		st.image(poster[5])
		st.write(name[5])
	
	with col2:
		st.image(poster[6])
		st.write(name[6])
	
	with col3:
		st.image(poster[7])
		st.write(name[7])
	with col4:
		st.image(poster[8])
		st.write(name[8])
		
	with col1:
		st.image(poster[9])
		st.write(name[9])
	
	with col2:
		st.image(poster[10])
		st.write(name[10])
	
	with col3:
		st.image(poster[11])
		st.write(name[11])
	with col4:
		st.image(poster[12])
		st.write(name[12])
