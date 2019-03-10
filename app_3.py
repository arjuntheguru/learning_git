class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.director = "Default Director"
        self.watched = watched

    def __repr__(self):
        return "<Movie: {}>".format(self.name)

    def json(self):
        return {
            'name':self.name,
            'genre': self.genre,
            'watched':self.watched
        }
    @classmethod    
    def from_json(cls, json_data):
        return Movie(**json_data)

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User: {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, True)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))
        #self.movies.remove()
    
    def watched_movies(self):
       movies_watched = list(filter(lambda movie:movie.watched, self.movies))
       return movies_watched

    def save_to_file(self):
        with open(self.name + ".txt",'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
              f.write(movie.name + "," + movie.genre + "," + str(movie.watched))
              f.write("\n")

    def json(self):
        return {
            'name':self.name,
            'movies':[
                 movie.json() for movie in self.movies 
            ]
        }
       
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user