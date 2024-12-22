
class Place :
    def __init__(self, numero, niveau, longueur, hauteur):
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur
        self.hauteur = hauteur
        self.disponnible = True
        self.pourSuperAbonne = False




    def estDisponible(self):
        return self.disponnible == True
    
    def setEstDisponible(self):
        if(self.estDisponible()):
            self.disponnible = False
        else:
            self.disponnible = True

    def estPourSuperAbonne(self):
        return self.pourSuperAbonne == True
    

    def setEstPourSuperAbonne(self):
       if(self.estPourSuperAbonne()):
            self.pourSuperAbonne = False
            
       else:
            self.pourSuperAbonne = True

    