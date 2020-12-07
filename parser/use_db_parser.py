import re

# create regular expression that matches the pattern for a valid use database statement


def buildRegExp():
    # captue use clause
    usedbre = "^([uU][sS][eE])"
    # database name
    dbname = "[a-zA-Z]+"
    return "{}\s+{}\s*$".format(usedbre, dbname)

# check if the statement is a valid use database statement


def isValidStatement(statement):
    usedb_pattern = buildRegExp()
    if re.match(usedb_pattern, statement):
        return True
    return False


def parse(statement):
    if isValidStatement(statement):
        return getDBName(statement)
    return False


# gets the database name
def getDBName(statement):
    words = statement.split(" ")
    for word in words:
        if word.lower() != "use" and word.lower() != "":
            return word
