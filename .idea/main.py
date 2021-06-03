# Press Umschalt+F10 to execute it or replace it with your code.
from com import COM
from time import sleep

if __name__ == '__main__':
    com=COM()
    com.port = "COM5"
    com.baudrate = 9600
    com.set_terminierung("\r")
    com.timeout = 0.3
    com.open()

    sleep(3)

    com.write("an")
    print(com.readline())
    sleep(2)
    com.write("aus")
    print(com.readline())
    sleep(2)

    com.close()
