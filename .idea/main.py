# Press Umschalt+F10 to execute it or replace it with your code.
from com import COM
from time import sleep
from terminal import Terminal
from tkinter import *
from plot import Plot

if __name__ == '__main__':
    fenster = Tk()

    L_frame = LabelFrame(fenster, text="Plot Kontrollfenster")
    L_frame.grid(column=0,row=0)
    R_frame = LabelFrame(fenster, text="Terminal")
    R_frame.grid(column=1, row=0)

    terminal = Terminal(R_frame,50)

    live_plot = Plot(L_frame)

    read_terminal = ""

    while True:
        terminal.update()
        live_plot.update()
        read_terminal = terminal.read_line()
        if read_terminal != "":
            #print(read_terminal)
            if read_terminal[:8] == "__plot__" and read_terminal[-1] == ";":
                try:
                    live_plot.insert(float(read_terminal[8:-1]))
                except:
                    pass
            else:
                terminal.insert("Rx> " + read_terminal)
            read_terminal = ""