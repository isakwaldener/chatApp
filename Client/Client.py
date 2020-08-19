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
        
        if not host:
            host = "127.0.0.1"
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
            self.gui.root_quit()


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
    
