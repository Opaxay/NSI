class Carre():

    def __init__(self, cote):
        """constructeur"""
        self.cote = cote


    def air(self):
        return self.cote * self.cote

    def perimetre(self):
        return self.cote * 4
    
    def changer_echelle(self, echelle):
        self.cote *= echelle 
        return self.cote
    
carre = Carre(3)
print(carre.perimetre())
print(carre.air())
print(carre.changer_echelle(2))