def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def wait_user_answer(self):
        print("Действия с фильмами")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('Создание фильма')
    def add_film(self):
        dict_movie = {
            "название фильма": None,
            "жанр фильма": None,
            "режиссера ": None,
            "год выпуска ": None,
            "длительность ": None,
            "студия ": None,
            "актеров ": None,

        }
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key}: ")
        return dict_movie

    @add_title('Список фильмов')
    def show_all_film(self, film):
        for ind, movie in enumerate(film, start=1):
            print(f"{ind}.  {movie}")

    @add_title('Названия фильма')
    def get_name_film(self):
        name_film = input("Введите название фильма ")
        return name_film

    @add_title('Просмотр фильма ')
    def show_one_movie(self, film):
        for key in film:
            print(f"{key}  - {film[key]}")

    @add_title('Сообщение об ошибке:')
    def show_incorrect_film_error(self, name_film):
        print(f"Фильма с названием {name_film} не существует")

    @add_title('Удаление фильма')
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удален")

    @add_title('Сообщение об ошибке:')
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")
