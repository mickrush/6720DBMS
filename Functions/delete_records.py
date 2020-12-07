import os 
import parsers.parser as parser
from structures.block import  Block
from structures.file import File
from structures.record import Record
import pickle


def deleteRecords(statement):
    res = parser.parse(statement)
    select_res = ""
    if res != False:
        table = res["table"]
        wc = res["where_condition"]
        print(wc)

        # path used for testing, table name should be passed to open function
        f = open("/Users/chanderpaulmartin/desktop/users", "rb")
        file = pickle.load(f) 

        table_columns = file.getColumns()
        
        # used to check which column is being operated on
        col_to_check  = -1
        col_check_type = ""
        
        for index, col in enumerate(table_columns, start=0):
            if wc[0] == col[0]:
                col_to_check = index
                col_check_type = col[1]

        # todo: refactor to put delete logic in block class
        
        for block in file.getBlocks():
            records = block.getRecords()
            for record in records: 
                if col_check_type == "int":
                    wc[2] = int(wc[2])
                    
                block.deleteRecord(col_to_check,wc[1], wc[2], col_check_type)
                
            print(block.getRecords())
            for record in  block.getRecords():
                print(record.getValues())

    return res != False


deleteRecords("delete from users where id = 3")

    

    