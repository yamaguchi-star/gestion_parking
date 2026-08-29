
import pydoc
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
       pass

pydoc.writedoc("voiture")



        

