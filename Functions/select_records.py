import os 
from structures.block import  Block
from structures.file import File
from structures.record import Record

def selectRecords(db, sel_cols, wc, file_obj):
  
    if db == "":
        return ""

    select_res = ""
    table_columns = file_obj.getColumns()

    indexes = []
    
    for i in sel_cols:
        for count, c in enumerate(table_columns):
            if i == c[0]:
                indexes.append(count)
                break
    
    for block in file_obj.getBlocks():
        for record in block.getRecords():
            record_values = record.getValues()
            for index in indexes:
                select_res += str(record_values[index]) + ""
            select_res += "\n"
  
    return select_res




    

    