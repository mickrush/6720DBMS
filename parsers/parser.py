import parsers.select_parser as sp
import parsers.create_db_parser as cdp
import parsers.create_table_parser as ctp
import parsers.delete_parser as dp
import parsers.insert_parser as itp
import parsers.update_parser as utp
import parsers.use_db_parser as udp


# returns result of the statement  being parsed
def parse(statement):
    statement_type = checkStatement(statement)
    if statement_type == "SELECT":
        return sp.parse(statement)
    elif statement_type == "CREATE_TABLE":
        return ctp.parse(statement)
    elif statement_type == "INSERT":
        return itp.parse(statement)
    elif statement_type == "UPDATE":
        return utp.parse(statement)
    elif statement_type == "DELETE":
        return dp.parse(statement)
    elif statement_type == "CREATE_DB":
        return cdp.parse(statement)
    elif statement_type == "USE_DB":
        return udp.parse(statement)
    elif statement_type == "VALID":
        return False


# checks which statement is being called
def checkStatement(statement):
    ls = statement.lower()
    if "select" in ls:
        return "SELECT"
    if "create table" in ls:
        return "CREATE_TABLE"
    if "insert" in ls:
        return "INSERT"
    if "update" in ls:
        return "UPDATE"
    if "delete" in ls:
        return "DELETE"
    if "create" in ls:
        return "CREATE_DB"
    if "use" in ls:
        return "USE_DB"
    return "INVALID"



# print("Select result: ", parse("select id, fname, lname, user from users"))
# print("Create table result: ", parse(
#     "create table users (id int, fname string, lname string)"))
# print("Insert result: ", parse("insert into users values (1, 'John', 'Brown')"))
# print("Delete result: ", parse("delete from users where id = 1"))
# print("Update result: ", parse("update users set fname = 'hello' where id = 3"))
# print("Create db result: ", parse("create users"))
# print("Use result: ", parse("use users"))
# print("Invalid statement result: ", parse("from users"))
