import tkinter


class Terminal(tkinter.Frame):
    def __init__(self, root, lines_length=100):
        super().__init__(root)
        self.scroll_org_frame = tkinter.Frame(root)
        self.scroll_org_frame.pack(side = "top")
        self.entry_org_frame = tkinter.Frame(root)
        self.entry_org_frame.pack(side="bottom", pady = 3)
        self.scroll_y = tkinter.Scrollbar(self.scroll_org_frame)
        self.scroll_y.pack(fill = "y", side = "right")
        self.scroll_x = tkinter.Scrollbar(self.scroll_org_frame, orient=tkinter.HORIZONTAL)
        self.scroll_x.pack(side="bottom", fill="x")
        self.listbox = tkinter.Listbox(self.scroll_org_frame, height=30, width=60)
        self.listbox.pack(side="top")
        self.scroll_y["command"] = self.listbox.yview
        self.scroll_x["command"] = self.listbox.xview
        self.listbox["yscrollcommand"] = self.scroll_y.set
        self.listbox["xscrollcommand"] = self.scroll_x.set
        self.entry = tkinter.Entry(self.entry_org_frame, width = 63)
        self.listbox.insert("end", *[i for i in range(100)])
        self.entry.pack()
        self.pack()

        self.max_length = lines_length
        self.autoscroll = False

    def insert(self, line):
        self.listbox.insert(tkinter.END, line)
        if self.listbox.size() > self.max_length:
            self.listbox.delete(0, self.listbox.size() - (self.max_length+1))
        if self.autoscroll == True:
            self.listbox.see(tkinter.END)

    def autoscroll_on(self):
        self.autoscroll = True

    def autoscroll_off(self):
        self.autoscroll = False

    def entry_enter_bind(self, para):
        print("enter")

    def entry_up_bind(self, para):
        print("up")

    def entry_down_bind(self, para):
        print("down")

    def entry_binding_init(self):
        self.entry.bind('<Return>', self.entry_enter_bind)
        self.entry.bind('<Up>', self.entry_up_bind)
        self.entry.bind('<Down>', self.entry_down_bind)
