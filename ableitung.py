
class Ableitung():
    def __init__(self):
        self.ungefiltert = []
        self.gefiltert = []


    def filtern(self, werte):
        self.gefiltert = []
        self.ungefiltert = werte
        for i, elem in enumerate(self.ungefiltert):
            if i < (len(self.ungefiltert) - 2):
                self.gefiltert.append(self.ungefiltert[i+1] - self.ungefiltert[i])
            else:
                break
        #print(self.gefiltert)
        return self.gefiltert