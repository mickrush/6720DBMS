import os 
import parsers.parser as parser
from structures.block import  Block
from structures.file import File
from structures.record import Record
import pickle


def insertRecord(db, values, file_obj):
    # res = parser.parse(statement)
    if db == "":
        return False
    added = False   
    record = Record(values[0], values[1], values[2])
    for block in file_obj.getBlocks():
        if block.addRecord(record):
            added = True
            break  
    return added


# insertRecord("insert into users values (3, 'John', 'Brown')")