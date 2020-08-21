import tkinter

class Enter_server:

    base_frame = None
    host_entry = None
    port_entry = None

    def __init__(self, gui, client):
        self.gui = gui
        self.client = client
        self.init_base_frame(gui.root)

    def init_base_frame(self, root):
        self.base_frame = tkinter.Frame(root)
        self.init_host_frame()
        self.init_port_frame()
        self.button()
        self.base_frame.pack()

    def init_host_frame(self):
        host_frame = tkinter.Frame(self.base_frame)
        host_label = self.label("Enter host")
        self.host_entry = self.entry_field()
        host_frame.pack()

    def init_port_frame(self):
        port_frame = tkinter.Frame(self.base_frame)
        port_label = self.label("Enter port")
        self.port_entry = self.entry_field()
        port_frame.pack()

    def button(self):
        button = tkinter.Button(self.base_frame, text="Join server",
                                command=self.join_server)
        button.pack()

    def join_server(self):
        self.gui.join_server(self.host_entry.get(), self.port_entry.get())

    def entry_field(self):
        entry = tkinter.Entry(self.base_frame)
        entry.pack()
        return entry

    def label(self, message):
        label = tkinter.Label(self.base_frame, text=message)
        label.pack()
        return label

    def destroy_enter_server_frame(self):
        self.base_frame.destroy()
