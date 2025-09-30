# 🎬 Intelligent Movie Recommender System

A personalized movie recommendation engine powered by collaborative filtering using **SVD** (via `surprise` library) and a lightweight Flask frontend. Built as a hands-on AI project and synced with the blog:  
👉 [Read the full article](https://dchobarkar.github.io/2024/09/21/hands-on-build-a-movie-recommender-in-python.html)

## 🚀 Live Demo

👉 [Try it on Render](https://movie-recommender-python-ehrd.onrender.com)

> Enter a `User ID` (like `1`, `10`, or `20`) and get a list of top-rated movie recommendations.

## 📦 Features

- 📊 Collaborative filtering with matrix factorization (SVD)
- 🎯 Predicts top-N movies per user with scores
- 🧠 Smart content-based fallback for title mapping
- 🌐 Deployed on Render with live web interface
- 🧪 Fully blog-synced — write as you build!

## 🛠️ Tech Stack

- Python 3.11
- Flask
- scikit-surprise
- pandas / NumPy / Matplotlib
- HTML / CSS (Jinja templates)
- Render (cloud deployment)

## 📁 Project Structure

```
movie-recommender-python/
├── data/                   # ratings.csv, movies.csv
├── notebooks/              # EDA and preprocessing notebooks
├── src/                    # Modular Python scripts
├── web/                    # Flask app + templates
│   ├── app.py
│   └── templates/
├── requirements.txt
└── README.md
```

## 🧪 Sample User IDs

Try the following user IDs to explore recommendations:

- `1`
- `10`
- `20`
- `50`
- `75`

## ⚙️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Flask app

```bash
cd web
python app.py
```

Then open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧪 Try the API

```bash
curl http://127.0.0.1:5000/api/recommend?userId=1
```

## 📚 Dataset Source

MovieLens 100K  
[https://grouplens.org/datasets/movielens/100k](https://grouplens.org/datasets/movielens/100k)

## 📝 License

MIT License

Made with ❤️ by [Darshan Jitendra Chobarkar](https://darshanwebdev.com)

## 💡 Author

Built by [Darshan Chobarkar](https://github.com/dchobarkar)  
Inspired by [this blog post](https://dchobarkar.github.io/2024/09/21/hands-on-build-a-movie-recommender-in-python.html)
