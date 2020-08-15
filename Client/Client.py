from GUI import GUI
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

class Client:
    
    # constants
    BUFSIZ = 1024

    def __init__(self):
        self.ADDR = None
        self.message = None
        self.msg_list = None
        self.socket = None
        self.gui = GUI(self)

    def set_message_list(self, listbox):
        self.msg_list = listbox

    def set_message(self, message):
        self.message.set(message)

    def set_socket(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(self.ADDR)

    def create_thread(self):
        receive_thread = Thread(target=self.receive_message)
        receive_thread.start()
        
    def setADDR(self, host, port):
        
        # HOST = input("Enter Host name:")
        # PORT = input("Enter port:")
        if not host:
            raise "Host is none"
        if not port:
           port = 33000
        self.ADDR = (host, port)

    def receive_message(self):
        while True:
            try:
                message = self.socket.recv(self.BUFSIZ).decode("utf8")
                self.msg_list.insert(tkinter.END, message)
            except OSError:
                break


    def send(self, event=None):
        msg = self.message.get()
        self.message.set("")
        self.socket.send(bytes(msg, "utf8"))
        if msg == "(QUIT)":
            self.socket.close()
            root.quit()


    def on_close(self, event=None):
        self.message.set("(QUIT)")
        self.send()


    def get_msg_list(self, mode=None):
        if(mode == "fast"):
            return tkinter.ListBox(msg_frame, height=10, width=50)
        else:
            return tkinter.Listbox(msg_frame, height=10, width=50,
                                   yscrollcommand=scrollbar)


def main():

    client = Client()
    client.gui.start_mainloop()

if __name__ == "__main__":
    main()

    
'''
root = tkinter.Tk()
root.title("This is a chatApp")
msg_frame = tkinter.Frame(root)
message = tkinter.StringVar()
message.set("Enter message here")
scrollbar = tkinter.Scrollbar(msg_frame)
msg_list = tkinter.Listbox(msg_frame, height=10, width=50,
                           yscrollcommand=scrollbar)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
msg_frame.pack()

entry_field = tkinter.Entry(root, textvariable=message)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(root, text="Send", command=send)
send_button.pack()
root.protocol("WM_DELETE_WINDOW", on_close)


HOST = input("Enter host: ")
PORT = input("Enter port: ")
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)
ADDR = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive_message)
receive_thread.start()
tkinter.mainloop()
'''
