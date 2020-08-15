import tkinter
# from Client import Client


class GUI:

    def __init__(self, client):
        self.client = client
        self.root = tkinter.Tk()
        self.root.title("This is a chat")
        self.enter_server()
        self.message_window()

    def start_mainloop(self):
        self.root.mainloop()

    def enter_server(self):
        enter_label = tkinter.Label(self.root, text="Enter host")
        enter_label.pack()
        e = tkinter.Entry(self.root)
        e.pack()
        port_label = tkinter.Label(self.root, text="Enter port")
        port_label.pack()
        e2 = tkinter.Entry(self.root)
        e2.pack()
        enter_button = tkinter.Button(self.root, text="confirm host",
                              command=lambda: self.join_server(e.get(),
                              e2.get()))
        enter_button.pack()

    def message_window(self):

        msg_frame = tkinter.Frame(self.root)
        self.client.message = tkinter.StringVar()
        self.client.set_message("Enter message here")
        scrollbar = tkinter.Scrollbar(msg_frame)
        self.client.set_message_list(tkinter.Listbox(msg_frame, height=10, 
                                     width=50, yscrollcommand=scrollbar))
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.client.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.client.msg_list.pack()
        msg_frame.pack()

        entry_field = tkinter.Entry(self.root,
                                    textvariable=self.client.message)
        entry_field.bind("<Return>", self.client.send)
        entry_field.pack()
        send_button = tkinter.Button(self.root, text="Send", 
                                     command=self.client.send)
        send_button.pack()

    def join_server(self, host, port):
        self.client.setADDR(host, port)
        self.client.set_socket()
        self.client.create_thread()

    def select_chat_room(self):
        button1 = Button(self.root, text="25 min timer")
        button1.pack()

        button2 = Button(self.root, text="5 min break")
        button2.pack()
