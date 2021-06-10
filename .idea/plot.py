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

        style.use('ggplot')
        self.fig = plt.figure(figsize=(10, 4), dpi=100)
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax1.set_ylim(self.y_min, self.y_max)
        self.line, = self.ax1.plot(self.x_plot, self.y_plot, 'b', marker='o', markersize=2, mec = 'r', mfc = 'r')

        self.plotcanvas = FigureCanvasTkAgg(self.fig, self)
        self.plotcanvas.get_tk_widget().grid(column=1, row=1)
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=50, blit=False)

        #gerbten frame packen
        self.pack()

    def animate(self, i):
        if len(self.y_plot) > self.x_limit:
            self.y_plot = self.y_plot[(len(self.y_plot)) - self.x_limit:]
        self.x_plot = range(len(self.y_plot))
        self.line.set_data(self.x_plot, self.y_plot)
        self.ax1.set_xlim(0, self.x_limit)

    def insert(self, elem):
        self.y_plot.append(elem)