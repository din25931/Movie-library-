## 3. Основной код (Movie.py)

`python
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os


class MovieLibrary:
    def init(self, root):
        self.root = root
        self.root.title("Movie Library")
        self.movies = []
        self.load_movies()
        self.setup_ui()

    def setup_ui(self):
        # Фрейм для добавления фильмов
        add_frame = ttk.LabelFrame(self.root, text="Добавить фильм")
        add_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(add_frame, text="Название:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.title_entry = ttk.Entry(add_frame, width=20)
        self.title_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(add_frame, text="Жанр:").grid(row=0, column=2, padx=5, pady=2, sticky="w")
        self.genre_entry = ttk.Entry(add_frame, width=15)
        self.genre_entry.grid(row=0, column=3, padx=5, pady=2)

        ttk.Label(add_frame, text="Год:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.year_entry = ttk.Entry(add_frame, width=10)
        self.year_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(add_frame, text="Рейтинг (0–10):").grid(row=1, column=2, padx=5, pady=2, sticky="w")
        self.rating_entry = ttk.Entry(add_frame, width=5)
        self.rating_entry.grid(row=1, column=3, padx=5, pady=2)

        ttk.Button(add_frame, text="Добавить", command=self.add_movie).grid(row=2, column=0, columnspan=4, pady=5)

        # Фрейм для фильтрации
        filter_frame = ttk.LabelFrame(self.root, text="Фильтрация")
        filter_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(filter_frame, text="Жанр:").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.filter_genre = ttk.Entry(filter_frame, width=15)
        self.filter_genre.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(filter_frame, text="Год:").grid(row=0, column=2, padx=5, pady=2, sticky="w")
        self.filter_year = ttk.Entry(filter_frame, width=10)
        self.filter_year.grid(row=0, column=3, padx=5, pady=2)

        ttk.Button(filter_frame, text="Применить фильтры", command=self.filter_movies).grid(row=0, column=4, padx=5)
        ttk.Button(filter_frame, text="Сбросить фильтры", command=self.reset_filters).grid(row=0, column=5, padx=5)

        # Таблица для отображения фильмов
        columns = ("Название", "Жанр", "Год", "Рейтинг")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Статус-бар
        self.status_var = tk.StringVar()
        self.status_var.set("Загружено фильмов: 0")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken")
        status_bar.pack(side="bottom", fill="x")

        self.update_table()

    def validate_input(self, title, genre, year, rating):
        """Проверка корректности ввода"""
        if not title or not genre:
            messagebox.showerror("Ошибка", "Название и жанр обязательны для заполнения!")
            return False
        try:
            year = int(year)
        except ValueError:
            messagebox.showerror("Ошибка", "Год должен быть числом!")
            return False
        try:
            rating = float(rating)
            if not 0 <= rating <= 10:
                messagebox.showerror("Ошибка", "Рейтинг должен быть от 0 до 10!")
                return False
        except ValueError:
            messagebox.showerror("Ошибка", "Рейтинг должен быть числом!")
            return False
        return True

    def add_movie(self):
        """Добавление нового фильма"""
        title = self.title_entry.get().strip()
        genre = self.genre_entry.get().strip()
        year = self.year_entry.get().strip()
        rating = self.rating_entry.get().strip() 
if self.validate_input(title, genre, year, rating):
            movie = {
                "title": title,
                "genre": genre,
                "year": int(year),
                "rating": float(rating)
            }
            self.movies.append(movie)
            self.save_movies()
            self.update_table()
            # Очистка полей ввода
            self.title_entry.delete(0, tk.END)
            self.genre_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.rating_entry.delete(0, tk.END)

    def filter_movies(self):
        """Фильтрация фильмов по жанру и/или году"""
        filter_genre = self.filter_genre.get().lower().strip()
        filter_year_str = self.filter_year.get().strip()

        filtered = []
        for movie in self.movies:
            genre_match = not filter_genre or filter_genre in movie["genre"].lower()
