import os

class File:

    def __init__(self, columns):
        self.blocks  = []
        self.columns = columns

    def addBlock(self, block):
        self.blocks.append(block)

    def getBlocks(self):
        return self.blocks

    