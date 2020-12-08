import os 
import parsers.parser as parser
from structures.block import  Block
from structures.file import File
import pickle


def MakeDB(path, statement):
#Use paths below based on operating system in os.chdir function
##Mac OS X: /Users/username/Desktop.
##Windows: C:/Users/username/Desktop.
##Linux: /home/username/Desktop.
##    os.chdir('Users/Bradley/Desktop')
    db = parser.parse(statement)
    try:
        os.mkdir(path + "/"+ db)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        return db
    return False

#TABLE CREATION
##make binary file
## check if false
def CreateTable(db,table_name, columns):
    #dict = parser.parse(statement)
    #check if file exist
    if db == "":
        return False
    if not os.path.exists(db+"/"+table_name):
        try:
            f = open(db + "/" + table_name,"wb")
            file = File(columns)
            file.addBlock(Block())
            file.addBlock(Block())
            file.addBlock(Block())
            pickle.dump(file, f)
            return True
        except FileNotFoundError:
            return False
    return False
            
# CreateTable("/Users/chanderpaulmartin/Desktop", "create table users (id int, fname string, lname string)")

# MakeDB("/Users/chanderpaulmartin/Desktop", "create shop")