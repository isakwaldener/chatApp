import tkinter


class GUI:

    msg_frame = None
    enter_server_frame = None

    def __init__(self, client):
        self.client = client
        self.root = tkinter.Tk()
        self.root.title("This is a chat")
        self.enter_server()

    def start_mainloop(self):
        self.root.mainloop()
    
    def root_quit(self):
        self.root.destroy()

    def enter_server(self):
        self.enter_server_frame = tkinter.Frame(self.root)
        enter_label = tkinter.Label(self.enter_server_frame, text="Enter host")
        enter_label.pack()
        e = tkinter.Entry(self.enter_server_frame)
        e.pack()
        port_label = tkinter.Label(self.enter_server_frame, text="Enter port")
        port_label.pack()
        e2 = tkinter.Entry(self.enter_server_frame)
        e2.pack()
        enter_button = tkinter.Button(self.enter_server_frame, text="confirm host",
                              command=lambda: self.join_server(e.get(),
                              e2.get()))
        enter_button.pack()
        self.enter_server_frame.pack()

    def destroy_msg_frame(self):
        self.msg_frame.destroy()
    
    def destroy_enter_server_frame(self):
        self.enter_server_frame.destroy()

    def message_window(self):

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
        self.destroy_enter_server_frame()
        self.message_window()
        self.client.setADDR(host, port)
        self.client.set_socket()
        self.client.create_thread()
        

    def select_chat_room(self):
        button1 = Button(self.root, text="25 min timer")
        button1.pack()

        button2 = Button(self.root, text="5 min break")
        button2.pack()
