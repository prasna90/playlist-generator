from os import listdir
from os.path import isfile, join

class Song_Name_Populator:
    
    def read_files_from_folder(self,path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles