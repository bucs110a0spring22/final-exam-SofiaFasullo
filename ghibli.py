import requests

class Ghibli:
  def __init__(self):
  self.api_url = 'https://ghibliapi.herokuapp.com/films'

  def get(self):
    self.r = requests.get(self.api_url)
    self.movies = self.r.json()

  def practice(self):
    self.problem = self.equations.get('expression')
    print((self.problem), '= ?')
    self.you_try = int(input("your answer:"))
    if self.you_try == self.equations.get('answer'):
      print("correct!")
    else:
      print("incorrect")
      print(self.equations.get('expression'), '=',self.equations.get('answer'))


'''
def main():
  r = requests.get('https://ghibliapi.herokuapp.com/films')
  print(r.status_code) #check for 200 'ok'
  movies = r.json()
  movie_index = random.randrange(0,21)
  print(movie_index)
  movie = movies[movie_index]
  for films in movie:
    print(films, ':', movie.get(films))
main()
'''