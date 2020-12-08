import os 
from structures.block import  Block
from structures.file import File
from structures.record import Record
import pickle


def insertRecord(db, values, file_obj):
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