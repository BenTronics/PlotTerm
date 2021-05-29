from serial import Serial

class COM(Serial):

    def __init__(self):
        super().__init__()