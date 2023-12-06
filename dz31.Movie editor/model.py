import pickle
import os.path


class Film:
    def __init__(self, name_film, genre, director, year_of_release, duration, atelier, the_actors):
        self.name_film = name_film
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.atelier = atelier
        self.the_actors = the_actors

    def __str__(self):
        return (f"{self.name_film} ({self.genre})\n "
                f"Режиссер - {self.director}\n "
                f"Год выпуска: {self.year_of_release}\n "
                f"Длительность: {self.duration}\n "
                f"Студия: {self.atelier}\n "
                f"Актеры: {self.the_actors}\n")


class MovieModel:
    def __init__(self):
        self.movie_name = "Movie.txt"
        self.movie = self.load_data()

    def add_movie(self, dict_movie):
        movie = Film(*dict_movie.values())
        self.movie[movie.name_film] = movie

    def get_all_the_movies(self):
        return self.movie.values()

    def get_single_movie(self, name_film):
        movie = self.movie[name_film]
        dict_movie = {
            "Название фильма:": movie.name_film,
            "Жанр:": movie.genre,
            "Режиссер:": movie.director,
            "Год выпуска:": movie.year_of_release,
            "Длительность:": movie.duration,
            "Студия:": movie.atelier,
            "Актеры:": movie.the_actors
        }
        return dict_movie

    def remove_movie(self, name_movie):
        return self.movie.pop(name_movie)

    def save_data(self):
        with open(self.movie_name, 'wb') as f:
            pickle.dump(self.movie, f)

    def load_data(self):
        if os.path.exists(self.movie_name):
            with open(self.movie_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
