import tkinter
from terminal import Terminal
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import randint

class Plot(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.x_plot = []
        self.y_plot = []
        self.x_limit = 100
        self.y_min = -1
        self.y_max = 1
        self.run = True

        style.use('ggplot')
        self.fig = plt.figure(figsize=(10, 5), dpi=100)
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax1.set_ylim(self.y_min, self.y_max)
        self.line, = self.ax1.plot(self.x_plot, self.y_plot, "b")

        self.plotcanvas = FigureCanvasTkAgg(self.fig, self)
        self.plotcanvas.get_tk_widget().grid(column=1, row=1)
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=50, blit=False)

        self.bedienung_org_frame = tkinter.Frame(root)
        self.bedienung_org_frame.grid()

        self.start_btn = tkinter.Button(self.bedienung_org_frame, text="Stop", bg="orange red", width=8, command=self.start_cmd)
        self.start_btn.grid(column=0, row=0)

        self.x_limit_entry = tkinter.Entry(self.bedienung_org_frame, width=5)
        self.x_limit_entry.grid(column=1, row=0)

        self.y_min_entry = tkinter.Entry(self.bedienung_org_frame, width=5)
        self.y_min_entry.grid(column=2, row=0)

        self.y_max_entry = tkinter.Entry(self.bedienung_org_frame, width=5)
        self.y_max_entry.grid(column=3, row=0)

        self.übernehmen_btn = tkinter.Button(self.bedienung_org_frame,text="Übernehmen", command=self.übernehmen_cmd)
        self.übernehmen_btn.grid(column=4, row=0)

        #gerbten frame packen
        self.grid()#pack()

    def animate(self, i):
        if len(self.y_plot) > self.x_limit:
            self.y_plot = self.y_plot[(len(self.y_plot)) - self.x_limit:]
        self.x_plot = range(len(self.y_plot))
        self.line.set_data(self.x_plot, self.y_plot)
        self.ax1.set_ylim(self.y_min, self.y_max)
        self.ax1.set_xlim(0, self.x_limit)

    def insert(self, elem):
        if self.run == True:
            self.y_plot.append(elem)

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