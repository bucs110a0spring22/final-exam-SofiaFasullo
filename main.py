#practice
import requests
#import random
import webbrowser
#from os import startfile
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
webbrowser.get(chrome).open_new('google.com')

def main():
  r = requests.get('https://random.dog/woof.json')
  #dog = r.json()
  print(r.status_code)
  dog = r.json()
  filepath = str(dog['url'])
  browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
  webbrowser.get(browser).open_new('google.com')
  
#main()
'''
def main():
  r = requests.get('https://x-math.herokuapp.com/api/random')
  print(r.status_code) #check for 200 'ok'
  equations = r.json()
  practice_prob = equations.get('expression')
  print((practice_prob), '= ?')
  you_try = int(input("your answer:"))
  if you_try == equations.get('answer'):
    print("correct!")
  else:
    print("incorrect")
    print(equations.get('expression'), '=',equations.get('answer'))
  #equation = equations[equation_index]
  #for i in equation:
  #  print(i, ':', equation.get(i))
main()
'''
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