# Press Umschalt+F10 to execute it or replace it with your code.
from com import COM
from time import sleep
from terminal import Terminal
from tkinter import *

if __name__ == '__main__':
    fenster = Tk()
    terminal = Terminal(fenster,50)

    while True:
        terminal.update()