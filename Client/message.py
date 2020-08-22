import tkinter

class message_frame:

    base_frame = None
    msg_entry = None

    def __init__(self, gui, client):
        self.gui = gui
        self.client = client
        self.create_base_frame(gui.root)

    def create_base_frame(self, root):
        self.base_frame = tkinter.Frame(root)
        self.msg_frame()
        self.button()
        self.base_frame.pack()

    def msg_frame(self):
        msg_frame = tkinter.Frame(self.base_frame)
        self.init_msg_list(msg_frame)
        self.entry(msg_frame)
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
        
    def entry(self, frame):
       self.msg_entry = tkinter.Entry(frame, textvariabl=self.client.message)
       self.msg_entry.bind("<Return>", self.client.send)
       self.msg_entry.pack()
    
    def button(self):
        button = tkinter.Button(self.base_frame, text="send", 
                                command=self.client.send)
        button.pack()
