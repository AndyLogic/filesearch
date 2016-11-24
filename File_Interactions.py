import os
import re


class FileSearch:
    """

    This is built to enable searching for a file based on a keyword.

    It will require the following:
    :param location: A string that is a valid file path
    :param keyword: A string of a keyword you are using to identify a file
    """

    def __init__(self, location, keyword):
        self.location = location
        self.keyword = keyword

    @staticmethod
    def files(directories, recursive):
        """
        This will collect all files in the location via a single directory or a recursive listing
        :param directories: is a list of folders
        :param recursive: requires a Yes(y) or No(n) string
        :return file_list: a list of files
        """

        file_list = []
        dir_list = directories
        if recursive.lower() == "n" or recursive.lower() == "no":
            for obj in os.listdir(dir_list[0]):
                try:
                    os.chdir(dir_list[0])
                except:
                    continue
                obj = os.path.abspath(obj)
                if os.path.isfile(obj):
                    yield obj
        else:
            while len(dir_list) > 0:
                folder = os.path.abspath(dir_list[0])
                try:
                    os.chdir(folder)
                except:
                    pass
                dir_list.pop(0)

                try:
                    checklist = os.listdir(folder)
                except:
                    pass

                while len(checklist) > 0:
                    obj = os.path.abspath(checklist[0])
                    checklist.pop(0)

                    if os.path.isdir(obj):
                        dir_list.append(obj)
                    else:
                      yield obj


    def search_location(self):
        """
        This will look for filenames with the keyword
        :return matched_files: a list of files found to have the keyword
        """
        matched_files = []
        for file in self.files([self.location], input("Do you want to search through sub-folders? ")):
            if re.search(self.keyword.lower(), os.path.basename(file).lower()):
                matched_files.append(file)

        return matched_files
