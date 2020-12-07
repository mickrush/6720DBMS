import re

# create regular expression that matches the pattern for a valid create database statement


def buildRegExp():
    # captue create clause
    createdbre = "^([cC][rR][eE][aA][tT][eE])"
    # database name
    dbname = "[a-zA-Z]+"
    return "{}\s+{}\s*$".format(createdbre, dbname)

# check if the statement is a valid create database statement


def isValidStatement(statement):
    createdb_pattern = buildRegExp()
    if re.match(createdb_pattern, statement):
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
        if word.lower() != "create" and word.lower() != "":
            return word
