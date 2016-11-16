import collections

class User_Interface:
  
  def __init__(self):
    self.search_history = collections.OrderedDict()
    
  def title_bar(title):
    print("-------------------------------")
    print(title)
    print("-------------------------------")
    
  def request(self):
    keyword = input("What keyword do you want to look for? ")
    location = input("What location do you wish to search? ")
    self.search_history[keyword] = location