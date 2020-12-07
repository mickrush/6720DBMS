import pickle
# from structures.file import File

f = open('/Users/chanderpaulmartin/desktop/users', 'rb')
print(f)
file = pickle.load(f)

print(file.columns)
print(file.getBlocks())

f.close()