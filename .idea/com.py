from serial import Serial

class COM(Serial):

    def __init__(self):
        super().__init__()
        self.terminierung = ""

    def get_terminierung(self):
        return self.terminierung

    def set_port(self):
        pass

    def set_terminierung(self, zeichen):
        self.terminierung = zeichen

    def write(self, msg):
        super().write((msg + self.terminierung).encode("utf-8"))