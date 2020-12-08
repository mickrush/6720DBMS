import os 
from structures.block import  Block
from structures.file import File
from structures.record import Record
import pickle


def updateRecords(db, sc, wc, file_obj):
    
    if db == "":
        return False
    
    table_columns = file_obj.getColumns()
    
    # used to get the column to update
    col_to_update = -1
    # used to check which column is being operated on
    col_to_check  = -1
    col_check_type = ""
    col_update_type = ""


    for index, col in enumerate(table_columns, start=0):
        if sc[0] == col[0]:
            col_to_update = index
            col_update_type = col[1]
        if wc[0] == col[0]:
            col_to_check = index
            col_check_type = col[1]

    # valid update statement but column to update or column to check does not exist
    # perform no update if either is true
    if col_to_check == -1 or col_to_update == -1:
        return False
    
    # todo: refactor to put update logic in block class
    for block in file_obj.getBlocks():
        for record in block.getRecords():
            record_values = record.getValues()
            if col_check_type == "int":
                wc[2] = int(wc[2])
                record_values[col_to_check] = int(record_values[col_to_check])
            if operate(record_values[col_to_check], wc[1], wc[2]): 
                record.update(col_to_update, sc[2])
             
    return True

# put in block class when refactoring
def operate(value1, operator, value2):
    if operator == "=":      
        return value1 == value2
    if operator == "!=":
        return value1 != value2
    if operator == ">":
        return value1 > value2
    if operator == "<":
        return value1 < value2

    

    