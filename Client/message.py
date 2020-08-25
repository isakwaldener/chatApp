import tkinter

class message_frame:

    def __init__(self, gui, client):
        self.gui = gui
        self.client = client
        self.base_frame = self.create_base_frame(gui.root)
        self.msg_entry = None

    def create_base_frame(self, root):
        base_frame = tkinter.Frame(root)
        self.create_msg_frame(base_frame)
        self.button(base_frame)
        base_frame.pack()
        return base_frame

    def create_msg_frame(self, frame):
        msg_frame = tkinter.Frame(frame)
        self.init_msg_list(msg_frame)
        self.create_entry(msg_frame)
        msg_frame.pack()

    def init_msg_list(self, frame):
        scrollbar = self.init_scrollbar(frame)
        self.client.init_message_list(tkinter.Listbox(frame, height=10, 
                                     width=50, yscrollcommand=scrollbar))
        self.client.msg_list.pack() 

    def init_scrollbar(self, frame):
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        return scrollbar
        
    def create_entry(self, frame):
        self.msg_entry = tkinter.Entry(frame, textvariabl=self.client.message)
        self.msg_entry.bind("<Return>", self.client.send)
        self.msg_entry.pack()
    
    def button(self, frame):
        button = tkinter.Button(frame, text="send", 
                                command=self.client.send)
        button.pack()
