import requests
import random

class Ghibli:
  def __init__(self):
    self.api_url = 'https://ghibliapi.herokuapp.com/films'

  def get(self):
    self.r = requests.get(self.api_url)
    self.movies = self.r.json()

  def hm(self):
    self.word = input("Write a keyword to search for a movie:")
    for i in range(0,21):
      self.films = self.movies[i]
      self.description = self.films.get('description')
      print(type(self.description))

  def search(self):
    self.word = char(input("Write a keyword to search for a movie:"))
    for i in range(0,21):
      self.films = self.movies[i]
      self.description = self.films.get('description')
      self.title = self.films.get('title')
      if self.word in self.description():
        print("A good choice would be ", self.title)

  def learn(self):
    self.choice = 0
    self.movie = self.movies[self.choice]
    for films in self.movie:
      print(films, ':', self.movie.get(films))

  def random(self):
    self.index = random.randrange(0,21)
    self.movie = self.movies[self.index]
    for films in self.movie:
      print(films, ':', self.movie.get(films))
