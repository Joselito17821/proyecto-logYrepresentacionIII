# 🎬 Sistema Inteligente de Recomendación de Películas

Un motor de recomendación de películas personalizado impulsado por filtrado colaborativo usando **SVD** (mediante la biblioteca `surprise`) y un frontend ligero en Flask. Construido como un proyecto práctico de IA y sincronizado con el blog:  
👉 [Lee el artículo completo](https://dchobarkar.github.io/2024/09/21/hands-on-build-a-movie-recommender-in-python.html)

## 🚀 Demo en vivo

👉 [Pruébalo en Render](https://movie-recommender-python-ehrd.onrender.com)

> Ingresa un `User ID` (como `1`, `10` o `20`) y obtén una lista de recomendaciones de películas mejor valoradas.

## 📦 Características

- 📊 Filtrado colaborativo con factorización matricial (SVD)
- 🎯 Predice top‑N películas por usuario con puntajes
- 🧠 Respaldo inteligente basado en contenido para el mapeo de títulos
- 🌐 Desplegado en Render con interfaz web en vivo
- 🧪 Totalmente sincronizado con el blog — escribe mientras construyes

## 🛠️ Tecnologías

- Python 3.11
- Flask
- scikit‑surprise
- pandas / NumPy / Matplotlib
- HTML / CSS (plantillas Jinja)
- Render (despliegue en la nube)

## 📁 Estructura del proyecto

    movie-recommender-python/
    ├── data/                   # ratings.csv, movies.csv
    ├── notebooks/              # EDA y cuadernos de preprocesamiento
    ├── src/                    # Scripts Python modulares
    ├── web/                    # App Flask + plantillas
    │   ├── app.py
    │   └── templates/
    │   └── static/
    ├── requirements.txt
    └── README.md

## 🧪 IDs de ejemplo

Prueba los siguientes `User ID` para explorar recomendaciones:

- `1`
- `10`
- `20`
- `50`
- `75`

## ⚙️ Cómo ejecutar

### 1. Instalar dependencias

    pip install -r requirements.txt

### 2. Iniciar la app Flask

    cd web
    python app.py

Luego abre tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧪 Probar la API

    curl http://127.0.0.1:5000/api/recommend?userId=1

## 📚 Fuente del dataset

MovieLens 100K  
[https://grouplens.org/datasets/movielens/100k](https://grouplens.org/datasets/movielens/100k)

## 📝 Licencia

MIT License

Hecho con ❤️ por [Darshan Jitendra Chobarkar](https://darshanwebdev.com)

## 💡 Autor

Creado por [Darshan Chobarkar](https://github.com/dchobarkar)  
Inspirado por [esta publicación del blog](https://dchobarkar.github.io/2024/09/21/hands-on-build-a-movie-recommender-in-python.html)

## 📄 Nota de adaptación

Cabe destacar que este ejemplo es una adaptación de un repositorio ya existente en GitHub: Movie‑Recommender‑System. Lo adapté para que fuera más sencillo de ejecutar y poder usarlo en este proyecto de Lógica y representación III.

La versión ajustada está disponible en mi propio repositorio: proyecto‑logYrepresentacionIII  
https://github.com/Joselito17821/proyecto-logYrepresentacionIII
