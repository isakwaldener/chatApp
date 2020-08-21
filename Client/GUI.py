import tkinter
from Enter_server import Enter_server

class GUI:

    msg_frame = None
    root = tkinter.Tk()


    def __init__(self, client):
        self.client = client
        self.init_root()
        self.enter_server = Enter_server(self, client)

    def start_mainloop(self):
        self.root.mainloop()

    def init_root(self):
        self.root.title("This is a chat")
        self.root.protocol("WM_DELETE_WINDOW", self.client.on_close)
    
    def root_quit(self):
        self.root.destroy()

    def entry_field_msg_frame(self):
        entry = tkinter.Entry(self.msg_frame)
        entry.pack()
        return entry
    
    def destroy_msg_frame(self):
        self.msg_frame.destroy()
    
    def initialize_frame(self, frame):
        frame = tkinter.Frame(self.root)
    
    def message_window_frame(self):

        self.msg_frame = tkinter.Frame(self.root)
        self.client.message = tkinter.StringVar()
        self.client.set_message("Enter message here")
        scrollbar = tkinter.Scrollbar(self.msg_frame)
        self.client.set_message_list(tkinter.Listbox(self.msg_frame, height=10, 
                                     width=50, yscrollcommand=scrollbar))
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.client.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.client.msg_list.pack()
        self.msg_frame.pack()

        entry_field = tkinter.Entry(self.root,
                                    textvariable=self.client.message)
        entry_field.bind("<Return>", self.client.send)
        entry_field.pack()
        send_button = tkinter.Button(self.root, text="Send", 
                                     command=self.client.send)
        send_button.pack()

    def join_server(self, host, port):
        self.enter_server.destroy_enter_server_frame()
        self.message_window_frame()
        self.client.setADDR(host, port)
        self.client.set_socket()
        self.client.create_thread()
        

    def select_chat_room(self):
        button1 = Button(self.root, text="25 min timer")
        button1.pack()

        button2 = Button(self.root, text="5 min break")
        button2.pack()
