import pickle
# from structures.file import File

f = open('/Users/chanderpaulmartin/desktop/users', 'rb')
print(f)
file = pickle.load(f)

print(file.columns)

for block in file.getBlocks():
    for record in block.getRecords():
        print (record.getValues())

f.close()