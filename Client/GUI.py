import tkinter
from Enter_server import Enter_server
from message import message_frame

class GUI:

    def __init__(self, client):
        self.client = client
        self.root = self.init_root() 
        self.enter_server = Enter_server(self, client)

    def start_mainloop(self):
        self.root.mainloop()

    def init_root(self):
        root = tkinter.Tk()
        root.title("This is a chat")
        root.protocol("WM_DELETE_WINDOW", self.client.on_close)
        return root
    
    def root_quit(self):
        self.root.destroy()

    def join_server(self, host, port):
        self.enter_server.destroy_enter_server_frame()
        self.create_message_frame()
        self.client.setADDR(host, port)
        self.client.set_socket()
        self.client.create_thread()
    
    def create_message_frame(self):
        msg_frame = message_frame(self, self.client)

