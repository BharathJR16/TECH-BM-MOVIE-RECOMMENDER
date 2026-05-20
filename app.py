import streamlit as st
import pickle
from rapidfuzz import process

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="TECH BM Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0E1117;
    color: white;
}

h1 {
    text-align: center;
    color: #E50914;
    font-size: 55px;
}

.search-text {
    text-align: center;
    color: lightgray;
    font-size: 20px;
}

.stTextInput > div > div > input {
    background-color: #1c1e26;
    color: white;
    border-radius: 10px;
    border: 2px solid #E50914;
    padding: 12px;
}

.stButton > button {
    width: 100%;
    background-color: #E50914;
    color: white;
    border-radius: 10px;
    font-size: 18px;
    border: none;
    padding: 10px;
}

.stButton > button:hover {
    background-color: #ff1f1f;
    color: white;
}

.movie-card {
    background-color: #1c1e26;
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(255,255,255,0.08);
}

.movie-title {
    color: white;
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
}

.movie-info {
    color: lightgray;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOAD DATA
# =========================================

movies = pickle.load(
    open('movie_list.pkl', 'rb')
)

similarity = pickle.load(
    open('similarity.pkl', 'rb')
)

# =========================================
# SESSION STATE
# =========================================

if 'selected_movie' not in st.session_state:

    st.session_state.selected_movie = None

# =========================================
# POSTER FUNCTION
# =========================================

def fetch_poster(movie_name):

    return (
        "https://dummyimage.com/"
        "300x450/000/ffffff&text="
        + movie_name.replace(" ", "+")
    )

# =========================================
# FIND CLOSEST MOVIE
# =========================================

def find_closest_movie(movie_name):

    movie_titles = movies['title'].tolist()

    closest_match = process.extractOne(
        movie_name,
        movie_titles
    )

    if closest_match:

        return closest_match[0]

    return None

# =========================================
# RECOMMEND FUNCTION
# =========================================

def recommend(movie):

    movie = find_closest_movie(movie)

    if movie is None:

        return None

    index = movies[
        movies['title'] == movie
    ].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:

        movie_data = movies.iloc[i[0]]

        recommendations.append({

            "title": movie_data.title,

            "rating": round(
                movie_data.vote_average,
                1
            ),

            "runtime": int(
                movie_data.runtime
            ),

            "genres": ", ".join(
                movie_data.genres
            ),

            "poster": fetch_poster(
                movie_data.title
            )
        })

    return movie, recommendations

# =========================================
# MOVIE DETAILS PAGE
# =========================================

if st.session_state.selected_movie is not None:

    movie = st.session_state.selected_movie

    st.title(movie['title'])

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            movie['poster'],
            width=320
        )

    with col2:

        st.subheader("🎬 Movie Details")

        st.write(
            f"⭐ Rating: {movie['rating']}"
        )

        st.write(
            f"⏱ Duration: {movie['runtime']} min"
        )

        st.write(
            f"🎭 Genre: {movie['genres']}"
        )

        st.write("")

        st.subheader("📖 Story")

        st.write(
            "This movie is recommended "
            "by the AI recommendation "
            "engine using Machine Learning."
        )

        st.write("")

        st.button(
            "▶ Watch Now"
        )

        st.write("")

        if st.button(
            "⬅ Back to Home"
        ):

            st.session_state.selected_movie = None
            st.rerun()

# =========================================
# HOME PAGE
# =========================================

else:

    # HEADER
    st.title(
        "🎬TECH BM Movie Recommender"
    )

    st.markdown(
        """
        <div class="search-text">
        Discover movies using Machine Learning 🍿
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # SEARCH BOX
    movie_name = st.text_input(
        "🔍 Enter Movie Name"
    )

    # BUTTON
    if st.button("Recommend Movies"):

        if movie_name == "":

            st.warning(
                "Please enter a movie name."
            )

        else:

            with st.spinner(
                "Finding awesome movies... 🍿"
            ):

                result = recommend(movie_name)

            if result is None:

                st.error(
                    "Movie not found."
                )

            else:

                matched_movie, recommendations = result

                st.success(
                    f"Showing results for: {matched_movie}"
                )

                st.write("")

                cols = st.columns(5)

                for idx, movie in enumerate(recommendations):

                    with cols[idx]:

                        st.image(
                            movie['poster']
                        )

                        st.markdown(
                            f"""
                            <div class="movie-card">

                            <div class="movie-title">
                            {movie['title']}
                            </div>

                            <div class="movie-info">
                            ⭐ Rating: {movie['rating']}
                            </div>

                            <div class="movie-info">
                            ⏱ Duration: {movie['runtime']} min
                            </div>

                            <div class="movie-info">
                            🎭 {movie['genres']}
                            </div>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        # VIEW BUTTON
                        if st.button(
                            f"View",
                            key=f"view_{idx}"
                        ):

                            st.session_state.selected_movie = movie
                            st.rerun()

# =========================================
# FOOTER
# =========================================

st.write("")
st.write("")

st.markdown(
    """
    <center style='color:gray;'>
    Built with Streamlit + Machine Learning 🚀
    </center>
    """,
    unsafe_allow_html=True
)