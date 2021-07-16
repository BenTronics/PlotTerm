from statistics import median

class Median():

    def __init__(self, breite=10):
        self.ungefiltert = []
        self.gefiltert = []
        self.fenster_breite = breite

    def filtern(self, werte):
        self.gefiltert = []
        self.ungefiltert = werte
        j = 0
        tmp = 0
        for i, elem in enumerate(self.ungefiltert):
            tmp = 0
            if((i+self.fenster_breite) < (len(self.ungefiltert)+1)):
                tmp = median(self.ungefiltert[i:i+self.fenster_breite])
                self.gefiltert.append(tmp)
            else:
                break
        return self.gefiltert

    def set_fenster_breite(self, breite):
        self.fenster_breite = breite