import re

# create regular expression that matches the pattern for a valid create table
# statement


def buildRegExp():
    # capture insert clause
    createre = "^([cC][rR][eE][aA][tT][eE]\s+[tT][aA][bB][lL][eE])"
    # capture table
    tablere = "[a-zA-Z]+"
    # capture values
    columnsre = "\(\s*([a-zA-Z]+\s+((int)|(string)))\s*(,\s*([a-zA-Z]+\s+((int)|(string)))){2}\s*\)"
    
    return "{}\s+{}\s+{}\s*$".format(createre, tablere, columnsre)


# check if the statement is a valid select statement


def isValidStatement(statement):
    create_table_pattern = buildRegExp()
    if re.match(create_table_pattern, statement):
        return True
    return False


def parse(statement):
    if isValidStatement(statement):
       table_name = getTable(statement)
       columns = getColumns(statement)
       return {"table": table_name, "columns": columns}
    # if the statement is not a valid statement then the parse method will return false
    return False

# get table name
def getTable(statement):
    words = statement.split()
    # table name will be third value in words array
    return words[2]


# gets the columns 
def getColumns(statement):
    # find the start of the values
   values_start = statement.find("(")
   # get values
   values = statement[values_start+1 : -1]
   # split by commas
   values = values.split(",")
   # return an array of arrays with the column name and data type
   return [(values[0]).split(), (values[1]).split(), (values[2]).split()]
   

