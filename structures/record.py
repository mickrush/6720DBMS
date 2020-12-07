class Record:

    def __init__(self, param1, param2, param3):
        self.values = [param1, param2, param3]
    
    
    def getValues(self):
        return self.values

    def update(self, col_number, value):
        self.values[col_number] = value