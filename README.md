# 🎬 TECH BM Movie Recommender

<div align="center">

<img src="https://img.icons8.com/color/480/netflix.png" width="120"/>

# 🍿 TECH BM Movie Recommender

### AI Powered Netflix-Style Movie Recommendation System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/UI-Netflix%20Style-black?style=for-the-badge"/>

</p>

---

### 🚀 Discover Amazing Movies Using Artificial Intelligence

✨ Smart Recommendations  
✨ Beautiful Interactive UI  
✨ Fast Fuzzy Search  
✨ Netflix Inspired Experience  

</div>

---

# 📖 Project Overview

TECH BM Movie Recommender is a Machine Learning based movie recommendation system that suggests movies similar to the one entered by the user.

The project uses:

- 🎬 Content-Based Filtering
- 🧠 Cosine Similarity
- ⚡ Machine Learning
- 🎨 Streamlit Web Application

The system analyzes movie metadata such as:

✅ Genres  
✅ Cast  
✅ Keywords  
✅ Director  
✅ Overview  

and recommends the most similar movies instantly.

---

# 🌟 Features

# 🎯 Smart Movie Search

Supports:

✅ Partial movie names  
✅ Wrong spellings  
✅ Similar text prediction  

### Example

| User Input | System Detects |
|---|---|
| spider man | Spider-Man 3 |
| avatr | Avatar |
| batmn | Batman |
| iron mn | Iron Man |

---

# 🎬 Recommendation Engine

The system provides:

✨ Top 5 Similar Movies  
✨ Movie Ratings  
✨ Runtime  
✨ Genres  
✨ Interactive Movie Cards  

---

# 🎨 Beautiful Netflix Style UI

The UI includes:

- Dark Theme 🌑
- Responsive Layout 📱
- Interactive Buttons 🎛
- Movie Detail Pages 🎥
- Smooth User Experience ⚡

---

# 🧠 Machine Learning Concept

## Content-Based Filtering

The recommendation system works by comparing movie features.

Movies with similar:

- Genres
- Cast
- Keywords
- Overview
- Directors

are recommended together.

---

# 📐 Similarity Metric Used

## Cosine Similarity

Cosine Similarity measures similarity between two movie vectors.

### Formula

\[
\cos(\theta)=\frac{A \cdot B}{||A|| ||B||}
\]

Where:

- A = Movie Vector 1
- B = Movie Vector 2

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend |
| Streamlit | Web Application |
| Pandas | Data Processing |
| Scikit-Learn | Machine Learning |
| RapidFuzz | Fuzzy Search |
| Pickle | Model Saving |

---

# 📂 Project Structure

```bash
TECH-BM-Movie-Recommender/
│
├── app.py
├── model.py
├── movie_list.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
└── README.md
