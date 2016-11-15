import collections

def main():
    print(search_details()[1])

def search_details():
    search_history = collections.OrderedDict()
    search_history[input("What keyword do you want to look for? ")] = input("What location do you wish to search? ")
    return search_history

if __name__ == '__main__':
    main()