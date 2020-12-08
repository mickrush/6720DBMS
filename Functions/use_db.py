import os 

def use_db(path, db):
    if os.path.exists(path+"/"+db):
        os.chdir(path+"/"+db)
        return  path+"/"+db    
    return False

# print(use_db("/Users/chanderpaulmartin/desktop", "use te"))