class Block:

    def __init__(self):
        self.records  = []

    def add(self, record):
        if len(self.records) < 5:
            self.records.append(record)

    def updateRecord(self):
        pass

    def deleteRecord(self):
        pass

    def isFull(self):
        pass

    