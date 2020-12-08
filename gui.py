from tkinter import *
from tkinter import messagebox
import socket


class GUI(object):
    def __init__(self, master, conn):
        self.master = master
        self.conn = conn

        # main frame
        self.main_frame = Frame(master, height=520, width=650, bg='#7FB3D5')
        self.main_frame.pack(fill=X)

        self.sql_lbl = Label(self.main_frame, text="SQL", bg='#7FB3D5')
        self.sql_lbl.place(x=40, y=40)
        self.sql_lbl.config(font=('Courier', 25))
        self.sql_input = Entry(self.main_frame, width=45, bd=0)
        self.sql_input.place(x=140, y=39)

        self.result_lbl = Label(self.main_frame, text="RESULT", bg='#7FB3D5')
        self.result_lbl.place(x=25, y=250)
        self.result_lbl.config(font=('Courier', 25))
        self.result_input = Text(
            self.main_frame, width=57, height=15, wrap=WORD)
        self.result_input.place(x=140, y=165)

        execute_btn = Button(self.main_frame, text="EXECUTE",
                             command=self.executeHandler)
        execute_btn.place(x=175, y=450)
        execute_btn.config(font=('Courier', 25))

        commit_btn = Button(self.main_frame, text="COMMIT",
                            command=self.commitHandler)
        commit_btn.place(x=380, y=450)
        commit_btn.config(font=('Courier', 25))

    def executeHandler(self):
        self.result_input.delete("1.0", "end")
        sql = self.sql_input.get()
        print("execute handler clicked")
        self.conn.sendall(sql.encode())
    
        msg = self.conn.recv(1024).decode()
        if msg != "":
            self.result_input.insert('1.0', msg)
        # else:
        #     messagebox.showinfo(
        #         "No SQL", "Please enter a valid sql statement", icon='info')

    def commitHandler(self):
        self.result_input.delete("1.0", "end")
        self.conn.sendall("commit".encode())

        msg = self.conn.recv(1024).decode()
        if msg != "":
            self.result_input.insert('1.0', msg)


def main():
    HOST = '127.0.0.1'
    PORT = 5879
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    root = Tk()
    app = GUI(root, s)
    root.title("DBMS Interface")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
