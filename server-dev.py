import socket
import random
import math
import hashlib
import time
import sys
import parsers.parser as parser
import Functions.DbCreation as dbc
import Functions.use_db as udb
import Functions.insert_record as isr
import Functions.select_records as sltr
import Functions.update_records as udpr
import Functions.delete_records as dltr
import pickle



def main():
    current_database = ""
    current_session = {}
    args = sys.argv
    HOST = '127.0.0.1'
    PORT = 5879
    path = str(args[1])
    print("The chosen path is: ", path)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print("connected by", addr)
            while True:
                statement = conn.recv(1024).decode()
                if not statement:
                    conn.close()

                # save changes to database
                if statement.lower() == "commit":
                    if current_database != "":
                        for key in current_session:
                            table = open(current_database + "/" + key, "wb")
                            pickle.dump(current_session[key], table)
                        conn.sendall("Changes saved to database".encode())
                    else:
                        conn.sendall("No database selected".encode())
                
                # create database
                if checkStatement(statement) == "CREATE_DB":
                    db = dbc.MakeDB(path, statement)
                    if db == False:
                        conn.sendall("Failed to create database".encode())
                        print(statement)
                    else:
                        msg = "Created database {}".format(db)
                        conn.sendall(msg.encode())
                
                # switch to database
                if checkStatement(statement) == "USE_DB":
                    db = parser.parse(statement)
                    if db != False:
                        switched = udb.use_db(path, db)
                        if switched!= False:
                            current_database = switched
                            msg = "Changed to database {}".format(current_database)
                            conn.sendall(msg.encode())
                        else:
                            conn.sendall("Could not change to database".encode())
                    else:
                        conn.sendall("Invalid use database statement".encode())

                # create table
                if checkStatement(statement) == "CREATE_TABLE":
                    res = parser.parse(statement)
                    if res != False:
                        created = dbc.CreateTable(current_database, res["table"], res["columns"])
                        if created:
                            msg = "Created table {}".format(res["table"])
                            conn.sendall(msg.encode())
                        else:
                            conn.sendall("Could not create table".encode())
                    else:
                        conn.sendall("Invalid create table statement".encode())
                        
                # insert into table
                if checkStatement(statement) == "INSERT":
                    res = parser.parse(statement)
                    if res != False:
                        table_name = res["table"]
                        values = res["values"]
                        inserted = False
                        if table_name in current_session:
                            inserted = isr.insertRecord(current_database, values, current_session[table_name])
                        else:
                            try:
                                table = open(current_database+"/"+table_name, "rb")
                                current_session[table_name] = pickle.load(table)
                                inserted = isr.insertRecord(current_database, values, current_session[table_name])
                                print(current_session)
                                table.close()
                            except FileNotFoundError:
                                conn.sendall("Table does not exist".encode())
                                continue
                            except:
                                conn.sendall("Table does not exist".encode())
                                continue
                        if inserted:
                            conn.sendall("Inserted record".encode())    
                        else:
                            conn.sendall("Could not insert record".encode())
                    else:
                        conn.sendall("Invalid insert statement".encode())
                
                # select records
                if checkStatement(statement) == "SELECT":
                    res = parser.parse(statement)
                    if res != False:
                        columns = res["columns"]
                        table_name = res["table"]
                        wc = res["where_condition"]
                        sel_res = ""
                        if table_name in current_session:
                            sel_res = sltr.selectRecords(current_database, columns, wc, current_session[table_name]) 
                        else:
                            try:
                                table = open(current_database+"/"+table_name, "rb")
                                current_session[table_name] = pickle.load(table)
                                sel_res = sltr.selectRecords(current_database, columns, wc, current_session[table_name])
                                table.close()
                            except FileNotFoundError:
                                conn.sendall("Table does not exist".encode())
                                continue
                            except:
                                conn.sendall("Table does not exist".encode())
                                continue
                        if sel_res != "":
                            conn.sendall(sel_res.encode())
                        else:
                            conn.sendall("There are no records".encode())
                    else:
                        conn.sendall("Invalid select statement".encode())

                # update records
                if checkStatement(statement) == "UPDATE":
                    res = parser.parse(statement)
                    if res != False:
                        table_name = res["table"]
                        sc = res["set_clause"]
                        wc = res["where_condition"]
                        if table_name in current_session:
                            upd_res = udpr.updateRecords(current_database, sc, wc, current_session[table_name]) 
                        else:
                            try:
                                table = open(current_database+"/"+table_name, "rb")
                                current_session[table_name] = pickle.load(table)
                                upd_res = udpr.updateRecords(current_database, sc, wc, current_session[table_name])
                                table.close()
                            except FileNotFoundError:
                                conn.sendall("Table does not exist".encode())
                                continue
                            except:
                                conn.sendall("Table does not exist".encode())
                                continue
                        if upd_res:
                            conn.sendall("Updated tables".encode())
                        else:
                            conn.sendall("No update".encode())                    
                    else:
                        conn.sendall("Invalid update statement".encode())

                # delete records
                if checkStatement(statement) == "DELETE":
                    res = parser.parse(statement)
                    if res != False:
                        table_name = res["table"]
                        wc = res["where_condition"]
                        if table_name in current_session:
                            upd_res = dltr.deleteRecords(current_database, wc, current_session[table_name]) 
                        else:
                            try:
                                table = open(current_database+"/"+table_name, "rb")
                                current_session[table_name] = pickle.load(table)
                                upd_res = dltr.deleteRecords(current_database, wc, current_session[table_name])
                                table.close()
                            except FileNotFoundError:
                                conn.sendall("Table does not exist".encode())
                                continue
                            except:
                                conn.sendall("Table does not exist".encode())
                                continue
                        if upd_res:
                            conn.sendall("Deleted record(s)".encode())
                        else:
                            conn.sendall("No delete".encode())                    
                    else:
                        conn.sendall("Invalid delete statement".encode())

                # any statement that's not one of the supported statements
                if checkStatement(statement) == "INVALID":
                    conn.sendall("Not a valid statement".encode())

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


if __name__ == "__main__":
    main()
