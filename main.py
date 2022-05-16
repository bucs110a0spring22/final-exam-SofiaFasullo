#practice
import requests
import random

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
def main():
    r = requests.get('https://opentdb.com/api.php?amount=1&category=18')
    trivia = r.json() #converts the data to a dictionary
    trivia = trivia['results'][0]
    for q in trivia:
        print(q, ':', trivia.get(q))
main()
'''
#https://ghibliapi.herokuapp.com