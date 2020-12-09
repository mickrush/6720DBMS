import re

# create regular expression that matches the pattern for a valid update
# statement


def buildRegExp():
    # capture select clause
    updatere = "^([uU][pP][dD][aA][tT][eE])"
    # capture table
    tablere = "[a-zA-Z]+"
    # capture set clause
    setre = "[sS][eE][tT]\s+([a-zA-Z]+\s+=\s+('[a-zA-Z]+'|\d+))"
    # capture where clause
    wherere = "([wW][hH][eE][rR][eE]\s+[a-zA-Z]+\s+(<|>|=|!=)\s+('[a-zA-Z]+'|\d+))"
    return "{}\s+{}\s+{}\s+{}\s*$".format(updatere, tablere, setre, wherere)


# check if the statement is a valid select statement


def isValidStatement(statement):
    update_pattern = buildRegExp()
    if re.match(update_pattern, statement):
        return True
    return False


def parse(statement):
    if isValidStatement(statement):
        table_name = getTable(statement)
        set_clause = getSetClause(statement)
        where_condition = getWhereCondition(statement)
        return {"table": table_name, "set_clause": set_clause, "where_condition": where_condition}
    return False


def getTable(statement):
    words = statement.split()
    return words[1]


# returns an array of 3 elements
# first element is column to be update
# second element the operator
# third element is value
def getSetClause(statement):
    set_index = statement.find("set")
    words = (statement[set_index+3:]).split()
    return [words[0], words[1], words[2]]


def getWhereCondition(statement):
    where_index = statement.find("where")
    # if where_index is less than 0 then there is no where clause
    if where_index < 0:
        return []
    condition = statement[where_index+5:]
    stripped = condition.strip()
    return stripped.split(" ")
