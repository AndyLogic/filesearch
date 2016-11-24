import collections
import File_Interactions

class User_Interface:

  def __init__(self):
    self.search_history = collections.OrderedDict()
    self.keyword = ""
    self.location = ""
    
  def title_bar(title):
    print("-------------------------------")
    print(title)
    print("-------------------------------")
    
  def request(self):
    self.keyword = input("What keyword do you want to look for? ")
    self.location = input("What location do you wish to search? ")

    return (self.location, self.keyword)






