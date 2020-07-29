from tkinter import Tk, Button, Label, Entry


class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Study timer")
        self.enter_server()


    def start_mainloop(self):
        self.root.mainloop()

    def enter_server(self):
        enter_label = Label(self.root, text="Enter server")
        enter_label.pack()
        e = Entry(self.root)
        e.pack() 
        enter_button = Button(self.root, text="Join server", command= lambda: self.join_server(e.get()))
        enter_button.pack()

    def join_server(self, addr):
        print(addr)

    def select_chat_room(self):
        button1 = Button(self.root, text="25 min timer")
        button1.pack()

        button2 = Button(self.root, text="5 min break")
        button2.pack()


if __name__ == "__main__":
    gui = GUI()
    gui.start_mainloop()