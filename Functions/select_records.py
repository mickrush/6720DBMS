import os 
import parsers.parser as parser
from structures.block import  Block
from structures.file import File
from structures.record import Record
import pickle


def selectRecords(statement):
    res = parser.parse(statement)
    select_res = ""
    if res != False:
        sel_cols = res["columns"]
        print(sel_cols)
        table = res["table"]
        wc = res["where_condition"]

        # path used for testing, table name should be passed to open function
        f = open("/Users/chanderpaulmartin/desktop/users", "rb")
        file = pickle.load(f) 

        table_columns = file.getColumns()

        indexes = []
        
        for i in sel_cols:
            for count, c in enumerate(table_columns):
                if i == c[0]:
                    indexes.append(count)
                    break
        
        for block in file.getBlocks():
            for record in block.getRecords():
                record_values = record.getValues()
                for index in indexes:
                    select_res += str(record_values[index]) + ""
                select_res += "\n"
        print(select_res)

    return select_res


selectRecords("select fname, id, lname from users")

    

    