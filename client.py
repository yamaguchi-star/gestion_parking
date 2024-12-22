from voiture import Voiture
from maintenance import Maintenance
from entretien import Entretien

class Client :
    def __init__(self, nom, adresse, modeP, estSuperAbonne=False):
        self.estAbonne = False
        self.estSuperAbonne = estSuperAbonne
        self.voiture = None
        self.nom = nom
        self.adresse = adresse
        self.mp = modeP

    def nouvellevoiture(self, voiture):
       
        self.voiture = voiture


    def isAbonne(self):
        return self.estAbonne == True
    
    def isSuperAbonne(self):
        return self.estSuperAbonne == True
    
    def setAbonne(self, abonnement):
        self.estAbonne = abonnement


    def setSuperAbonne(self, abonnement):
        self.estSuperAbonne = abonnement


    def Desabonner(self, abonnement):
       self.estAbonne = abonnement


    def demanderMaintenance(self):
       main = Maintenance("2020-08_12","2020-08_12",'string')
       main.effectuerMaintenance()
       print(main)

    def demanderEntretien(self):
        entretien = Entretien("2020-08_12","2020-08_12",'string')
        entretien.effectuenEntretien()
        print(entretien)

    def demanderLivraison(self, dateLivraison, heure, adresseLiv):
        pass 


    def sortirParking(self, parking, ticket):
        parking.libererPlace(ticket['place'])

    def EntrerParking(self, parking):
        return parking.seGarer(self)
        

    def affiche(self):
        print(self.voiture.immatirculation)







        