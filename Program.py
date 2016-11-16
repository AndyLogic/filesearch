from User_Interface import *

def main():
  repeat = "Y"
  User_Interface.title_bar("File Search")
  
  a = User_Interface()
  while repeat.lower() == "y" or repeat.lower() == "yes":
    a.request()
    repeat = input("Would you like to search again?")
  
  print(a.search_history)
  
  
if __name__ == '__main__':
    main()