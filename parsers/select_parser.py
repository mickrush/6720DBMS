import re

# create regular expression that matches the pattern for a valid select
# statement


def buildRegExp():
    # capture select clause
    selectre = "^([sS][eE][lL][eE][cC][tT])"
    # capture columns
    columnsre = "([a-z]+(,\\s*[a-z]+)*)"
    # capture from clause
    fromre = "(from){1}"
    # capture table name
    tablere = "[a-zA-Z]+"
    # capture where clause
    wherere = "((\s+((where)\s+[a-zA-Z]+\s+(<|>|=|!=)\s+('[a-zA-Z]+'|\d+)))??)"
    # builds select statement pattern
    return "{}\s+{}\s+{}\s+{}{}\s*$".format(selectre, columnsre, fromre, tablere, wherere)

# check if the statement is a valid select statement


def isValidStatement(statement):
    select_pattern = buildRegExp()
    if re.match(select_pattern, statement):
        return True
    return False


def parse(statement):
    if isValidStatement(statement):
        columns = getColumns(statement)
        table_name = getTable(statement)
        where_condition = getWhereCondition(statement)
        return {"columns": columns, "table": table_name, "where_condition": where_condition}
    # if the statement is not a valid statement then the parse method will return false
    return False


def getTable(statement):
    transformed = re.sub(",", " ", statement)
    count = 0
    words = transformed.split()
    for word in words:
        if word.lower() == "from":
            return words[count+1]
        count += 1


# gets all the columns specified in the select statement
def getColumns(statement):
    columns = []
    # remove commas
    transformed = re.sub(",", " ", statement)
    # split statement into an array of words
    for word in transformed.split(" "):
        # if the current word is 'from' then there are no more columns
        if word.lower() == "from":
            break
        else:
            if word not in [",", " ", "select", ""]:
                columns.append(word)
    return columns

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
