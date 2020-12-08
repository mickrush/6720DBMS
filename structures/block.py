class Block:

    def __init__(self):
        self.records  = []

    def addRecord(self, record):
        if not self.isFull():
            self.records.append(record)
            return True
        
        return False

    def updateRecord(self):
        pass
    
    # needs editing, leaving one value
    def deleteRecord(self, col_to_check, operator, value, col_check_type):
        for index, record in enumerate(self.records):
            if col_check_type == "int":
                record.getValues()[col_to_check] = int(record.getValues()[col_to_check])
            if operate(record.getValues()[col_to_check], operator, value):
                del self.records[index]



    def getRecords(self):
        return self.records

    def isFull(self):
        return len(self.records) == 5

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


    