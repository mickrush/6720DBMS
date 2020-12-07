import os 
import parsers.parser as parser
from structures.block import  Block
from structures.file import File
from structures.record import Record
import pickle


def insertRecord(statement):
    res = parser.parse(statement)
    added = False
    if res != False:
        
        table_name = res["table"]
        values = res["values"]
        # in working version, the table_name will be pased since the application would be in the
        # database directory and have direct access to the files
        f = open("/Users/chanderpaulmartin/desktop/users", "rb")
       
    
        file = pickle.load(f) 

        
        record = Record(values[0], values[1], values[2])
 
        for block in file.getBlocks():
            print(block)
            if block.addRecord(record):
                added = True
                pickle.dump(file, open("/Users/chanderpaulmartin/desktop/users", 'wb'))
                print("Record was added")
                break  
    return added


insertRecord("insert into users values (1, 'John', 'Brown')")