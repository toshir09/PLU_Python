# 5. Movie Recommendation System
### Problem Statement
# A streaming platform stores movie information.
# Each movie contains
# * Movie ID
# * Title
# * Genre
# * Rating
# * Watch Count
# ### Requirements
# 1. Fetch all movies.
# 2. Sort movies based on Rating.
# 3. Search a movie using Movie ID.
# 4. Display Top 10 highest-rated movies.
# 5. Display the most watched movie in every genre.
# ### Concepts
# * Sorting
# * Searching
# * Dictionaries
# * SQL GROUP BY
import sqlite3
# Movie Class
class Movie:
    def __init__(self, movie_id, title, genre, rating, watch_count):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watch_count = watch_count
    def display(self):
        print("--------------------------------------------")
        print("Movie ID     :", self.movie_id)
        print("Title        :", self.title)
        print("Genre        :", self.genre)
        print("Rating       :", self.rating)
        print("Watch Count  :", self.watch_count)
# Create SQLite Database
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
movie_id INTEGER PRIMARY KEY,
title TEXT,
genre TEXT,
rating REAL,
watch_count INTEGER
)
""")
cursor.execute("DELETE FROM movies")
movies = [
(101,"pushpa1","Action",9.2,5000),
(102,"Titanic","Romance",8.8,7500),
(103,"Avengers","Action",9.0,9000),
(104,"yogi","Action",9.5,8000),
(105,"Bahubali","Action",8.9,9500),
(106,"Frozen","Animation",8.2,6000),
(107,"Toy Story","Animation",8.7,7000),
(108,"Joker","Drama",9.1,8500),
(109,"bahubali2","Comedy",9.4,9200),
(110,"KGF","Action",8.6,9800),
(111,"bunny","Animation",9.0,7200),
(112,"Avatar","Sci-Fi",8.9,8800)
]
cursor.executemany("INSERT INTO movies VALUES(?,?,?,?,?)", movies)
conn.commit()
# Fetch Movies
cursor.execute("SELECT * FROM movies")
rows = cursor.fetchall()
movie_list = []
for row in rows:
    movie_list.append(Movie(*row))
# Sort Movies by Rating
movie_list.sort(key=lambda x: x.rating, reverse=True)
print("\nMovies Sorted By Rating\n")
for movie in movie_list:
    movie.display()
# Binary Search
movie_list.sort(key=lambda x: x.movie_id)
def binary_search(arr, key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid].movie_id == key:
            return arr[mid]
        elif arr[mid].movie_id < key:
            low = mid+1
        else:
            high = mid-1
    return None
try:
    movie_id = int(input("\nEnter Movie ID to Search : "))
except ValueError:
    print("Invalid Movie ID")
    conn.close()
    exit()
result = binary_search(movie_list, movie_id)
if result:
    print("\nMovie Found\n")
    result.display()
else:
    print("\nMovie Not Found")
# Top 10 Highest Rated Movies
movie_list.sort(key=lambda x: x.rating, reverse=True)
print("\nTop 10 Highest Rated Movies\n")
for movie in movie_list[:10]:
    movie.display()
# Most Watched Movie in Every Genre
print("\nMost Watched Movie in Every Genre\n")
cursor.execute("""
SELECT genre,title,MAX(watch_count)
FROM movies
GROUP BY genre
""")
rows = cursor.fetchall()
movie_dict = {}
for row in rows:
    movie_dict[row[0]] = (row[1], row[2])
for genre in movie_dict:
    print("--------------------------------------------")
    print("Genre       :", genre)
    print("Movie       :", movie_dict[genre][0])
    print("Watch Count :", movie_dict[genre][1])
conn.close()