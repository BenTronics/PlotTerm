class BefehlsVerlauf:

    def __init__(self, max_num):
        self.befehle = []
        self.lese_pointer = 0
        self.max_num = max_num

    def append(self, elem):
        self.befehle.append(elem)
        if len(self.befehle) > self.max_num:
            self.befehle = self.befehle[1:]
        self.lese_pointer = len(self.befehle) - 1

    def pointer_up(self):
        if self.lese_pointer >= 1:
            self.lese_pointer -= 1

    def pointer_down(self):
        if self.lese_pointer < (len(self.befehle) - 1):
            self.lese_pointer += 1

    def read(self):
        return self.befehle[self.lese_pointer]