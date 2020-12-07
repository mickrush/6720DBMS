import os 
import parsers.parser as parser


def use_db(path, statement):
    db = parser.parse(statement)
    if db != False:
        if os.path.exists(path+"/"+db):
            os.chdir(path+"/"+db)
            return True      
    return False

print(use_db("/Users/chanderpaulmartin/desktop", "use te"))