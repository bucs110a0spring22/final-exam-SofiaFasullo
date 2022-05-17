import requests

class Tutor:
  def __init__(self):
    self.api_url = 'https://x-math.herokuapp.com/api/random'

  def get(self):
    self.r = requests.get(self.api_url)
    self.equations = self.r.json()

  def practice(self):
    self.problem = self.equations.get('expression')
    print((self.problem), '= ?')
    self.you_try = int(input("your answer:"))
    if self.you_try == self.equations.get('answer'):
      print("correct!")
    else:
      print("incorrect")
      print(self.equations.get('expression'), '=',self.equations.get('answer'))