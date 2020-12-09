import re

# create regular expression that matches the pattern for a valid delete
# statement


def buildRegExp():
    # capture select clause
    deletere = "^([dD][eE][lL][eE][tT][eE])"
    # capture from clause
    fromre = "([fF][rR][oO][mM]\s+[a-zA-Z]+)"
    # capture where clause
    wherere = "([wW][hH][eE][rR][eE]\s+[a-zA-Z]+\s+(<|>|=|!=)\s+('[a-zA-Z]+'|\d+))"
    return "{}\s+{}\s+{}\s*$".format(deletere, fromre, wherere)


# check if the statement is a valid delete statement


def isValidStatement(statement):
    delete_pattern = buildRegExp()
    if re.match(delete_pattern, statement):
        return True
    return False


def parse(statement):
    if isValidStatement(statement):
        table_name = getTable(statement)
        where_condition = getWhereCondition(statement)
        return {"table": table_name, "where_condition": where_condition}
    return False


def getTable(statement):
    words = statement.split()
    return words[2]

# gets the where clause condition
# returns an array with the first element being
# the column, second operator, third value


def getWhereCondition(statement):
    where_index = statement.find("where")
    # if where_index is less than 0 then there is no where clause
    if where_index < 0:
        return []
    condition = statement[where_index+5:]
    stripped = condition.strip()
    return stripped.split(" ")
