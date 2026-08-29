
from place import Place

class Voiture:

    def __init__(self, hauteur, longueur, immatriculation):
        self.hauteur = hauteur
        self.longueur = longueur
        self.immatirculation = immatriculation
        self.estDansParkine = False


    def addPlacementVoiture(self, placement):

       pass



    def setEstDansParking(self, etat):
        self.estDansParkine = etat


    def getImmatirculation(self):
        return self.immatirculation
       

    def getHauteur(self):
        return self.hauteur
        
    def getLongueur(self):
         return self.longueur
    
    def getEstDansParrking(self):
        return self.estDansParkine


        

