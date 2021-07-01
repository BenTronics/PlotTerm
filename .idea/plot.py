import tkinter
from terminal import Terminal
from matplotlib import pyplot as plt
from matplotlib import style

class Plot(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.x_plot = []
        self.y_plot = []
        self.x_limit = 100
        self.y_min = -1
        self.y_max = 1
        self.run = True
        self.y_autoscale = False
        self.marker_pos = 1

        style.use('ggplot')
        self.fig = plt.figure(figsize=(10, 5), dpi=100)
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax1.set_ylim(self.y_min, self.y_max)
        self.line, = self.ax1.plot(self.x_plot, self.y_plot, "b")


        self.bedienung_org_frame = tkinter.Frame(root)
        self.bedienung_org_frame.grid()

        self.start_btn = tkinter.Button(self.bedienung_org_frame, text="Stop", bg="orange red", command=self.start_cmd, width=40, pady=20)
        self.start_btn.grid(column=0, row=1, columnspan=3)

        self.x_limit_entry = tkinter.Entry(self.bedienung_org_frame, width=5)
        self.x_limit_entry.grid(column=0, row=3)
        self.x_limit_entry.insert(0, self.x_limit)

        self.y_min_entry = tkinter.Entry(self.bedienung_org_frame, width=5)
        self.y_min_entry.grid(column=1, row=3)
        self.y_min_entry.insert(0, self.y_min)

        self.y_max_entry = tkinter.Entry(self.bedienung_org_frame, width=5)
        self.y_max_entry.grid(column=2, row=3)
        self.y_max_entry.insert(0, self.y_max)

        self.x_limit_label = tkinter.Label(self.bedienung_org_frame, text="X Limit", padx=10, pady=20)
        self.x_limit_label.grid(column=0, row=2)

        self.y_min_label = tkinter.Label(self.bedienung_org_frame, text="Y Min", padx=10, pady=20)
        self.y_min_label.grid(column=1, row=2)

        self.y_max_label = tkinter.Label(self.bedienung_org_frame, text="Y Max", padx=10, pady=20)
        self.y_max_label.grid(column=2, row=2)

        self.übernehmen_btn = tkinter.Button(self.bedienung_org_frame,text="Übernehmen", command=self.übernehmen_cmd, width=40, pady=20)
        self.übernehmen_btn.grid(column=0, row=4, columnspan=3)

        self.scroll_org_frame = tkinter.Frame(root)
        self.scroll_org_frame.grid(column=0, row=5, columnspan=3)
        self.entry_org_frame = tkinter.Frame(self.scroll_org_frame)
        self.entry_org_frame.pack(side="bottom", pady=3)
        self.scroll_y = tkinter.Scrollbar(self.scroll_org_frame)
        self.scroll_y.pack(fill="y", side="right")
        self.listbox = tkinter.Listbox(self.scroll_org_frame, height=21, width=45)
        self.listbox.pack(side="top")
        self.scroll_y["command"] = self.listbox.yview
        self.listbox["yscrollcommand"] = self.scroll_y.set

        self.x_limit_entry.bind('<Return>', self.x_limit_enter_bind)
        self.y_min_entry.bind('<Return>', self.y_min_enter_bind)
        self.y_max_entry.bind('<Return>', self.y_max_enter_bind)

        #gerbten frame packen
        self.grid()#pack()


    def update(self):
        if len(self.y_plot) > self.x_limit:
            self.y_plot = self.y_plot[(len(self.y_plot)) - self.x_limit:]
        self.x_plot = range(len(self.y_plot))
        self.ax1.set_ylim([self.y_min, self.y_max])
        if self.run == True:
            self.ax1.clear()
            plt.plot(self.y_plot, "b")
            if self.y_autoscale == False:
                plt.ylim(self.y_min, self.y_max)
            else:
                if len(self.y_plot) > 1:
                    plt.ylim(min(self.y_plot), max(self.y_plot))
            plt.pause(0.01)
        elif self.run == False and len(self.y_plot) > 1:
            if self.marker_pos != int(self.listbox.index(tkinter.ANCHOR)) and self.listbox.index(tkinter.ANCHOR) < len(self.y_plot):
                plt.draw()
            self.marker_pos = int(self.listbox.index(tkinter.ANCHOR))
            if self.marker_pos > len(self.y_plot)-1:
                self.marker_pos -= 1
            self.ax1.clear()
            plt.plot(self.x_plot[:self.marker_pos+1], self.y_plot[:self.marker_pos+1], "b")
            plt.plot(self.x_plot[self.marker_pos], self.y_plot[self.marker_pos], "bo", markersize=6, markeredgecolor="r")
            plt.plot(self.x_plot[self.marker_pos:], self.y_plot[self.marker_pos:], "b")

    def insert(self, elem):
        if self.run == True:
            self.y_plot.append(elem)
            self.listbox.insert(tkinter.END, str(elem))
            self.listbox.see(tkinter.END)
            if len(self.y_plot) > self.x_limit:
                self.listbox.delete(0, self.listbox.size() - (self.max_length+1))


    def start_cmd(self):
        if self.start_btn["text"] == "Stop":
            self.run = False
            self.start_btn["text"] = "Start"
            self.start_btn["bg"] = "lime green"
        else:
            self.run = True
            self.start_btn["text"] = "Stop"
            self.start_btn["bg"] = "orange red"

    def set_x_limit(self, limit):
        self.x_limit = limit

    def set_y_min(self, min):
        self.y_min = min

    def set_y_max(self, max):
        self.y_max = max

    def übernehmen_cmd(self):
        try:
            self.set_x_limit(int(self.x_limit_entry.get()))
        except:
            pass
        try:
            self.set_y_max(float(self.y_max_entry.get()))
        except:
            pass
        try:
            self.set_y_min(float(self.y_min_entry.get()))
        except:
            pass

    def x_limit_enter_bind(self, para):
        try:
            self.set_x_limit(int(self.x_limit_entry.get()))
        except:
            pass

    def y_max_enter_bind(self, para):
        try:
            self.set_y_max(float(self.y_max_entry.get()))
        except:
            pass

    def y_min_enter_bind(self, para):
        try:
            self.set_y_min(float(self.y_min_entry.get()))
        except:
            pass