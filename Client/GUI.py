import tkinter


class GUI:

    msg_frame = None
    enter_server_frame = None
    root = tkinter.Tk()
    host_entry = None
    port_entry = None
    port = None
    host = None


    def __init__(self, client):
        self.client = client
        self.init_root()
        self.enter_server_frame()

    def start_mainloop(self):
        self.root.mainloop()

    def init_root(self):
        self.root.title("This is a chat")
        self.root.protocol("WM_DELETE_WINDOW", self.client.on_close)
    
    def root_quit(self):
        self.root.destroy()

    def enter_server_entry_field(self):
        entry = tkinter.Entry(self.enter_server_frame)
        entry.pack()
        return entry

    def entry_field_msg_frame(self):
        entry = tkinter.Entry(self.msg_frame)
        entry.pack()
        return entry
    
    def enter_server_label(self, message):
        label = tkinter.Label(self.enter_server_frame, text=message)
        label.pack()
        return label

    def enter_server_button(self):
        button = tkinter.Button(self.enter_server_frame, text="Join server",
                                command=self.join_server)
        button.pack()
        return button

    def set_port_and_host(self):
        self.port = self.port_entry.get()
        self.host = self.host_entry.get()
        
    def enter_server_frame(self):
        self.enter_server_frame = tkinter.Frame(self.root)
        host_label = self.enter_server_label("Enter host")
        self.host_entry = self.enter_server_entry_field()
        port_label = self.enter_server_label("Enter port")
        self.port_entry = self.enter_server_entry_field()
        enter_button = self.enter_server_button()
        self.enter_server_frame.pack()

    def destroy_msg_frame(self):
        self.msg_frame.destroy()
    
    def destroy_enter_server_frame(self):
        self.enter_server_frame.destroy()

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

    def join_server(self):
        self.set_port_and_host()
        self.destroy_enter_server_frame()
        self.message_window_frame()
        self.client.setADDR(self.host, self.port)
        self.client.set_socket()
        self.client.create_thread()
        

    def select_chat_room(self):
        button1 = Button(self.root, text="25 min timer")
        button1.pack()

        button2 = Button(self.root, text="5 min break")
        button2.pack()
