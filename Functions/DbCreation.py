import os 
import create_table_parser
#DATABASE CREATION
##def Create Path()


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

    dict = create_table_parser.parse(statement)
    if dict != False:
            table_name = dict["table"]
            values = dict["values"]
            f = open(path + "/" + table_name,"ab")
            print("Table created %s "%path)
            
