import os 
import parsers.parser as parser
from structures.block import  Block
from structures.file import File
import pickle


def MakeDB(path,dbname):
#Use paths below based on operating system in os.chdir function
##Mac OS X: /Users/username/Desktop.
##Windows: C:/Users/username/Desktop.
##Linux: /home/username/Desktop.

##    os.chdir('Users/Bradley/Desktop')

    os.chdir(path)
    
    dbname = dbname

    try:
        os.mkdir(dbname)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        return path 

#TABLE CREATION
##make binary file
## check if false
def CreateTable(path,statement):

    dict = parser.parse(statement)
    if dict != False:
            table_name = dict["table"]
            columns = dict["values"]
            f = open(path + "/" + table_name,"wb")
            print("Table created %s "%path)
            file = File(columns)
            file.addBlock(Block())
            file.addBlock(Block())
            file.addBlock(Block())
            pickle.dump(file, f)
            
CreateTable("/Users/chanderpaulmartin/Desktop", "create table users (id int, fname string, lname string)")