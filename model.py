import pandas as pd
import ast
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Load Datasets
# ==========================================

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# ==========================================
# Merge Both Datasets
# ==========================================

movies = movies.merge(credits, on='title')

# ==========================================
# Select Important Columns
# ==========================================

movies = movies[['movie_id',
                 'title',
                 'overview',
                 'genres',
                 'keywords',
                 'cast',
                 'crew',
                 'vote_average',
                 'runtime']]

# ==========================================
# Remove Null Values
# ==========================================

movies.dropna(inplace=True)

# ==========================================
# Helper Functions
# ==========================================

# Convert genres/keywords JSON to list
def convert(text):

    L = []

    for i in ast.literal_eval(text):

        L.append(i['name'])

    return L


# Get top 3 cast members
def convert_cast(text):

    L = []

    counter = 0

    for i in ast.literal_eval(text):

        if counter != 3:

            L.append(i['name'])

            counter += 1

        else:
            break

    return L


# Fetch Director Name
def fetch_director(text):

    L = []

    for i in ast.literal_eval(text):

        if i['job'] == 'Director':

            L.append(i['name'])

    return L


# ==========================================
# Apply Functions
# ==========================================

movies['genres'] = movies['genres'].apply(convert)

movies['keywords'] = movies['keywords'].apply(convert)

movies['cast'] = movies['cast'].apply(convert_cast)

movies['crew'] = movies['crew'].apply(fetch_director)

# ==========================================
# Convert Overview to List
# ==========================================

movies['overview'] = movies['overview'].apply(lambda x: x.split())

# ==========================================
# Remove Spaces Between Words
# Example:
# Sam Worthington -> SamWorthington
# ==========================================

movies['genres'] = movies['genres'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies['keywords'] = movies['keywords'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies['cast'] = movies['cast'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies['crew'] = movies['crew'].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

# ==========================================
# Create Tags Column
# Combine all features
# ==========================================

movies['tags'] = movies['overview'] + \
                 movies['genres'] + \
                 movies['keywords'] + \
                 movies['cast'] + \
                 movies['crew']

# ==========================================
# Create New DataFrame
# ==========================================

new_df = movies[['movie_id',
                 'title',
                 'tags',
                 'genres',
                 'vote_average',
                 'runtime']]

# ==========================================
# Convert List to String
# ==========================================

new_df['tags'] = new_df['tags'].apply(
    lambda x: " ".join(x)
)

# Convert to lowercase
new_df['tags'] = new_df['tags'].apply(
    lambda x: x.lower()
)

# ==========================================
# Vectorization
# ==========================================

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = cv.fit_transform(
    new_df['tags']
).toarray()

# ==========================================
# Cosine Similarity
# ==========================================

similarity = cosine_similarity(vectors)

# ==========================================
# Save Files Using Pickle
# ==========================================

pickle.dump(
    new_df,
    open('movie_list.pkl', 'wb')
)

pickle.dump(
    similarity,
    open('similarity.pkl', 'wb')
)

# ==========================================
# Success Message
# ==========================================

print("===================================")
print("Movie Recommendation Model Created")
print("===================================")

print("Files Saved Successfully:")
print("1. movie_list.pkl")
print("2. similarity.pkl")