import re

# create regular expression that matches the pattern for a valid insert
# statement


def buildRegExp():
    # capture insert clause
    insertre = "^([iI][nN][sS][eE][rR][tT])"
    # capture into clause
    intore = "([iI][nN][tT][oO]\s+[a-zA-Z]+)"
    # capture values
    valuesre = "[vV][aA][lL][uU][eE][sS]\s+(\((('[a-zA-Z]+'|\d+)\s*(,\s*('[a-zA-Z]+'|\d+))*)\))"
   
   
    return "{}\s+{}\s+{}\s*$".format(insertre, intore, valuesre)


# check if the statement is a valid select statement


def isValidStatement(statement):
    insert_pattern = buildRegExp()
    if re.match(insert_pattern, statement):
        return True
    return False


def parse(statement):
    if isValidStatement(statement):
       table_name = getTable(statement)
       values = getValues(statement)
       return {"table": table_name, "values": values}
    # if the statement is not a valid statement then the parse method will return false
    return False

# get table name
def getTable(statement):
    words = statement.split()
    # table name will be third value in words array
    return words[2]


# gets the values to be inserted into the table
def getValues(statement):
    # find the start of the values
   values_start = statement.find("(")
   # get values
   values = statement[values_start+1 : -1]
   # remove commas
   values = re.sub(",", " ", values)
   # return an array with the values
   return values.split()
   

