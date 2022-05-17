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