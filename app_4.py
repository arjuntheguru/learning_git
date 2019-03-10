from app_3 import Movie
from app_3 import User


my_movie = Movie("The Matrix","Sci-Fi", True)
user = User("Jose")
user.movies.append(my_movie)
user.add_movie("Hello","World")
print(user.watched_movies())
user.delete_movie("The Matrix")
print(user.watched_movies())