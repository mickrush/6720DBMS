import socket
import random
import math
import hashlib
import time
import sys
import parsers.parser as parser
import Functions.DbCreation as dbc
import Functions.use_db as udb



def main():
    current_database = ""
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
                        conn.sendall("Could not change to database".encode())

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
                        conn.sendall("Could not create table".encode())
                        



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
