# Press Umschalt+F10 to execute it or replace it with your code.
from com import COM
from time import sleep
from terminal import Terminal
from tkinter import *

if __name__ == '__main__':
    com=COM()
    com.port = "COM5"
    com.baudrate = 9600
    com.set_terminierung("\r")
    com.timeout = 0.3
    """
    com.open()

    sleep(3)

    com.write("an")
    print(com.readline())
    sleep(2)
    com.write("aus")
    print(com.readline())
    sleep(2)

    com.close()
    """

    fenster = Tk()
    terminal = Terminal(fenster,50)
    terminal.entry_binding_init()
    terminal.insert("test /////////////////////////////////////////////////////6666666666666666666666666666666666666666666666666666")
    fenster.mainloop()