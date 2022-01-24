from os import listdir
from os.path import isfile, join

class FileOperator:
    
    #Class Attribute
    Operation = "File Operations"
    
    def read_files(self,path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles
    