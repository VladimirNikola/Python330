from view import UserInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.film_model = MovieModel()
        self.interface = UserInterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.interface.add_film()
            self.film_model.add_movie(film)
        elif answer == "2":
            film = self.film_model.get_all_the_movies()
            self.interface.show_all_film(film)
        elif answer == "3":
            film_title = self.interface.get_name_film()
            try:
                film = self.film_model.get_single_movie(film_title)
            except KeyError:
                self.interface.show_incorrect_film_error(film_title)
            else:
                self.interface.show_one_movie(film)
        elif answer == "4":
            film_title = self.interface.get_name_film()
            try:
                title = self.film_model.remove_movie(film_title)
            except KeyError:
                self.interface.show_incorrect_film_error(film_title)
            else:
                self.interface.remove_single_film(title)
        elif answer == "q":
            self.film_model.save_data()
        else:
            self.interface.show_incorrect_answer_error(answer)
