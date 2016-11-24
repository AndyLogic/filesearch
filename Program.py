from User_Interface import *

def main():
  repeat = "Y"
  User_Interface.title_bar("File Search")
  
  a = User_Interface()
  while repeat.lower() == "y" or repeat.lower() == "yes":
    user_input = a.request()
    user_files = File_Interactions.FileSearch(user_input[0],user_input[1])
    User_Interface.title_bar("Found Files")
    print("\n".join(user_files.search_location()))
    User_Interface.title_bar("Search Again")
    repeat = input("would you like to repeat? Type yes or no")
    ##print("The keyword is {} and the location {}".format(user_input[0],user_input[1]))

if __name__ == '__main__':
    main()