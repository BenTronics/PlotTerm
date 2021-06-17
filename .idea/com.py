import serial
import serial.tools.list_ports

class COM(serial.Serial):

    def __init__(self):
        super().__init__()
        self.terminierung = "\r"

    def get_terminierung(self):
        return self.terminierung

    def set_port(self):
        pass

    def set_terminierung(self, zeichen):
        self.terminierung = zeichen

    def write(self, msg):
        super().write((msg + self.terminierung).encode("utf-8"))

    def list_ports(self):
        ports = []
        for port in (serial.tools.list_ports.comports()):
            ports.append(int((str(port)[3:]).split(" ", 1)[0]))
        return ports