import os

class Block:

    def __init__(self):
        self.records  = []

    def add(self, record):
        if len(self.records) < 5:
            self.records.append(record)

    def updateRecord(self, column, condition, condition_value,value):
        column_number = getColumnNumber(column)
        if column_number > -1:
            for record in self.records:
                if self.match(record, condition, condition_value):
                    record.update(column_number, value)

        
    def getColumnNumber(self, column):
        column_number = 0
        for file_column in File.getColumns():
            if column = file_column:
                return column_number
            column_number += 1
        # if -1 is returned column is not found
        return -1