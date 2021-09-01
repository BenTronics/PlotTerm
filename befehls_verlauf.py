class BefehlsVerlauf:

    def __init__(self, max_num):
        self.befehle = []
        self.pointer = 0
        self.max_num = max_num

    def append(self, elem):
        #Elemnet nicht aufnehmen, wenn es dem letzten eingetragenem Element entspricht
        if len(self.befehle) > 0:
            if elem == self.befehle[self.pointer]:
                return
        self.befehle.append(elem)
        if len(self.befehle) > self.max_num:
            self.befehle = self.befehle[1:]
        self.pointer = len(self.befehle) - 1

    def pointer_up(self):
        if self.pointer >= 1:
            self.pointer -= 1

    def pointer_down(self):
        if self.pointer < (len(self.befehle) - 1):
            self.pointer += 1

    def read(self):
        return self.befehle[self.pointer]