class Record:

    def __init__(self):

        self.values = []


    def add(self, value1, value2, value3):
        self.values.append(value1)
        self.values.append(value2)
        self.values.append(value3)

    def update(self, column_number, value):
        self.records[column_number] = value