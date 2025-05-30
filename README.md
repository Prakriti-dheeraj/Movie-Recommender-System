# Movie-Recommender-System

🎬 TMDB 5000 Movies Dataset - Content-Based Movie Recommendation System
📌 Project Overview
This project performs data cleaning and transformation on the TMDB 5000 Movies Dataset to prepare it for building a content-based movie recommendation system. The goal is to combine textual and categorical features like genres, cast, crew, keywords, and overview to create a feature-rich dataset that can be used to recommend similar movies.

📁 Dataset
tmdb_5000_movies.csv: Contains movie metadata such as genres, keywords, budget, revenue, popularity, etc.

tmdb_5000_credits.csv: Contains detailed cast and crew information for each movie.

📊 Data Processing Steps
Merging Datasets
The two datasets (movies and credits) are merged on the title column to form a unified dataframe.

Selecting Useful Columns
The following columns are retained for analysis:

movie_id

title

overview

genres

keywords

cast

crew

Handling Missing Data

Rows with null overview values are dropped.

Duplicate entries are checked and removed if found.

Parsing Complex Columns
Columns like genres, keywords, cast, and crew are stored as stringified JSON. These are parsed using ast.literal_eval() and transformed into clean, usable lists.

Column Transformations

Genres & Keywords: Converted to lists of names.

Cast: Limited to the top 3 actors.

Crew: Only the director is extracted.

🛠️ Technologies Used
Python 3

Pandas — for data manipulation

Ast — for parsing stringified lists/dictionaries

Jupyter Notebook — for exploratory programming and documentation

🧠 What’s Next?
This cleaned and transformed dataset is ideal for creating a content-based filtering recommendation system using:

TF-IDF / Bag of Words on overview

Combining genres, keywords, cast, and director for similarity scoring

Cosine similarity for movie-to-movie recommendations

▶️ How to Run
Clone the repository or download the dataset.

Install necessary libraries:

bash
Copy
Edit
pip install pandas
Open the notebook and run the cells to preprocess the data:

bash
Copy
Edit
jupyter notebook
📌 Sample Output (after preprocessing)
title	genres	cast	director
Avatar	[Action, Adventure, Fantasy, Sci-Fi]	[Sam Worthington, Zoe Saldana]	James Cameron
Pirates of the Caribbean	[Adventure, Fantasy, Action]	[Johnny Depp, Orlando Bloom]	Gore Verbinski

📜 License
This project is for educational and research purposes, using publicly available data from Kaggle.
