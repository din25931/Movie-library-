import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class MovieLibrary:
    def __init__(self, master):
        self.master = master
        self.master.title("Личная кинотека")

        # Поля ввода
        self.title_label = tk.Label(master, text="Название:")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=0, column=1)

        self.genre_label = tk.Label(master, text="Жанр:")
        self.genre_label.grid(row=1, column=0)
        self.genre_entry = tk.Entry(master)
        self.genre_entry.grid(row=1, column=1)

        self.year_label = tk.Label(master, text="Год выпуска:")
        self.year_label.grid(row=2, column=0)
        self.year_entry = tk.Entry(master)
        self.year_entry.grid(row=2, column=1)

        self.rating_label = tk.Label(master, text="Рейтинг (0-10):")
        self.rating_label.grid(row=3, column=0)
        self.rating_entry = tk.Entry(master)
        self.rating_entry.grid(row=3, column=1)

        # Кнопка добавления фильма
        self.add_button = tk.Button(master, text="Добавить фильм", command=self.add_movie)
        self.add_button.grid(row=4, columnspan=2)

        # Таблица для отображения фильмов
        self.movie_tree = ttk.Treeview(master, columns=("title", "genre", "year", "rating"), show='headings')
        self.movie_tree.heading("title", text="Название")
        self.movie_tree.heading("genre", text="Жанр")
        self.movie_tree.heading("year", text="Год выпуска")
        self.movie_tree.heading("rating", text="Рейтинг")
        self.movie_tree.grid(row=5, columnspan=2)

        # Загрузка данных из файла
        self.movies = []
        self.load_movies()

    def add_movie(self):
        title = self.title_entry.get().strip()
        genre = self.genre_entry.get().strip()
        
        try:
            year = int(self.year_entry.get().strip())
            if year < 1888:  # Первый фильм был снят в 1888 году
                raise ValueError("Год должен быть больше 1888.")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Год выпуска должен быть числом.")
            return

        try:
            rating = float(self.rating_entry.get().strip())
            if rating < 0 or rating > 10:
                raise ValueError("Рейтинг должен быть от 0 до 10.")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Рейтинг должен быть числом от 0 до 10.")
            return

        movie = {"title": title, "genre": genre, "year": year, "rating": rating}
        self.movies.append(movie)
        self.update_movie_list()
        self.save_movies()
        
        # Очистка полей ввода
        self.clear_entries()

    def update_movie_list(self):
        for row in self.movie_tree.get_children():
            self.movie_tree.delete(row)
        
        for movie in self.movies:
            self.movie_tree.insert("", "end", values=(movie["title"], movie["genre"], movie["year"], movie["rating"]))

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

    def save_movies(self):
        with open('movies.json', 'w') as f:
            json.dump(self.movies, f)

    def load_movies(self):
        if os.path.exists('movies.json'):
            with open('movies.json', 'r') as f:
                self.movies = json.load(f)
                self.update_movie_list()
        app = MovieLibrary(root)
    root.mainloop()

    self.filter_genre_label = tk.Label(master, text="Фильтр по жанру:")
    self.filter_genre_label.grid(row=6, column=0)
    self.filter_genre_entry = tk.Entry(master)
    self.filter_genre_entry.grid(row=6, column=1)

    self.filter_year_label = tk.Label(master, text="Фильтр по году:")
    self.filter_year_label.grid(row=7, column=0)
    self.filter_year_entry = tk.Entry(master)
    self.filter_year_entry.grid(row=7, column=1)

    self.filter_button = tk.Button(master, text="Фильтровать", command=self.filter_movies)
    self.filter_button.grid(row=8, columnspan=2)

def filter_movies(self):
    genre_filter = self.filter_genre_entry.get().strip()
    year_filter = self.filter_year_entry.get().strip()

    filtered_movies = []
    
    for movie in self.movies:
        if (not genre_filter or genre_filter.lower() in movie["genre"].lower()) and 
           (not year_filter or str(movie["year"]) == year_filter):
            filtered_movies.append(movie)

    for row in self.movie_tree.get_children():
        self.movie_tree.delete(row)

    for movie in filtered_movies:
        self.movie_tree.insert("", "end", values=(movie["title"], movie["genre"], movie["year"], movie["

if __name__ == "__main__":
    root = tk.Tk()
