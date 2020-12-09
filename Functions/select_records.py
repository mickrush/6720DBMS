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
    
    if len(wc) == 0:
 
        for block in file_obj.getBlocks():
            for record in block.getRecords():
                record_values = record.getValues()
                for index in indexes:
                    select_res += str(record_values[index]) + ""
                select_res += "\n"
    else:
        col_to_check  = -1
        col_check_type = ""
        for index, col in enumerate(table_columns, start=0):
            if wc[0] == col[0]:
                col_to_check = index
                col_check_type = col[1]

        for block in file_obj.getBlocks():
            for record in block.getRecords():
                record_values = record.getValues()
                if col_check_type == "int":
                    wc[2] = int(wc[2])
                    record_values[col_to_check] = int(record_values[col_to_check])
                if operate(record_values[col_to_check], wc[1], wc[2]): 
                    for index in indexes:
                        select_res += str(record_values[index]) + ""
                select_res += "\n"
  
    return select_res




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


    