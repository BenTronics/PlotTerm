# Press Umschalt+F10 to execute it or replace it with your code.
from com import COM
from time import sleep
from terminal import Terminal
from tkinter import *
from plot import Plot

if __name__ == '__main__':
    fenster = Tk()

    L_frame = Frame(fenster)
    L_frame.grid(column=0,row=0)
    R_frame = LabelFrame(fenster, text="Terminal")
    R_frame.grid(column=1, row=0)

    terminal = Terminal(R_frame,50)

    p = Plot(L_frame)

    read_terminal = ""

    while True:
        #p.update()
        #p.animate(1)
        terminal.update()
        read_terminal = terminal.read_line()
        if read_terminal != "":
            if read_terminal.find("__plot__") != -1:
                #print(read_terminal[8:])
                try:
                    p.insert(float(read_terminal[8:]))
                except:
                    pass
            else:
                terminal.insert(read_terminal)
            read_terminal = ""