import tkinter

class Enter_server:

    def __init__(self, gui, client):
        self.gui = gui
        self.client = client
        self.host_entry = None
        self.port_entry = None
        self.base_frame = self.init_base_frame(gui.root)
        

    def init_base_frame(self, root):
        base_frame = tkinter.Frame(root)
        self.init_host_frame(base_frame)
        self.init_port_frame(base_frame)
        self.button(base_frame)
        base_frame.pack()
        return base_frame

    def init_host_frame(self, frame):
        host_frame = tkinter.Frame(frame)
        host_label = self.label(frame, "Enter host")
        self.host_entry = self.entry_field(frame)
        host_frame.pack()

    def init_port_frame(self, frame):
        port_frame = tkinter.Frame(frame)
        port_label = self.label(frame, "Enter port")
        self.port_entry = self.entry_field(frame)
        port_frame.pack()

    def button(self, frame):
        button = tkinter.Button(frame, text="Join server",
                                command=self.join_server)
        button.pack()

    def join_server(self):
        self.gui.join_server(self.host_entry.get(), self.port_entry.get())

    def entry_field(self, frame):
        entry = tkinter.Entry(frame)
        entry.pack()
        return entry

    def label(self, frame, message):
        label = tkinter.Label(frame, text=message)
        label.pack()
        return label

    def destroy_enter_server_frame(self):
        self.base_frame.destroy()
