from place import Place
class Parking:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_instanceParking(cls):
        return cls._instance


    def __init__(self, nbplaceParNiveau, nbPlaces):
        
        self.nbplaceParNiveau = nbplaceParNiveau
        self.nbPlaces = nbPlaces
        self.nbrePlacesLibre = nbPlaces
        self.listePlace = dict()
        self.initaliserPlacesDansParking()
        self.listeAbonnes = dict()
        self.ParckGarentie = list()

    def creerPlace(self, place):
        idplace = place.niveau+str(place.numero) 
        self.listePlace[idplace] = place


    def affiche(self):
       for id, place in self.listePlace.items():
           print(id, place.numero)

    def initaliserPlacesDansParking(self):
        for i in range(self.nbPlaces):
            place = Place(i, "A", (3+i)%6, (2+i)%6)
            self.creerPlace(place)

    def proposerAbonnement(self, client, idplace):
         while True:
            print("----------Bienvenue proprietaire de : ", client.voiture.immatirculation)
            print("\n--- Menu ---")
            print("1. Devenir SuperAbonne")
            print("2. Devenir Abonne")
            print("3. Quitter")

            choix = int(input("Entrer votre choix : "))

            if choix == 1:
                client.setSuperAbonne(True)
                self.listeAbonnes[idplace] = client.voiture.immatirculation
                self.listePlace[idplace].setEstPourSuperAbonne()
            elif (choix == 2):
                client.setAbonne(True)

            elif choix == 3:
                 print("Merci d'avoir utilisé le système de gestion du parking. À bientôt !")
                 break
            else:
                 print("Option invalide. Veuillez réessayer.")



    def seGarer(self, c1):
       
            if self.nbrePlacesLibre >0 :
                for idplace, place in self.listePlace.items():
                    if ((c1.voiture.hauteur <= place.hauteur) and (c1.voiture.longueur <= place.longueur) and place.estDisponible()):
                        self.nbrePlacesLibre -=1
                        place.setEstDisponible()
                        print("Voiture garée à la place ", idplace)
                        c1.voiture.setEstDansParking(True)
                        self.proposerAbonnement(c1, idplace)
                        return idplace
                else :
                    print("Desolé, cette voiture ne peut etre garée dans ce parking : ", c1.voiture.immatirculation)
            if c1.isSuperAbonne():
                if c1.isSuperAbonne() and not c1.voiture.getEstDansParrking():
                    self.ParckGarentie.append(c1)
                else:
                   print("Parking is plein")
      # else:  
             #print("Binevenu vous etes super abonne") 
             #for id, place in self.listePlace.items():
                 # if place.estPourSuperAbonne():
                   # if self.listeAbonnes[id] == c1.voiture.immatirculation:
                    #    place.setEstDisponible()
                      #  c1.voiture.setEstDansParking(True)
                      #  self.nbrePlacesLibre -=1
                       # return id
            
                      

    def libererPlace(self, id):
        self.listePlace[id].disponnible = True

    
    def affichePlaceDisponnible(self):
        place = [id for id, place in self.listePlace.items() if place.estDisponible()]
        print(place)



    def getPlace(self, idplace):
        if (idplace is not None):
         return self.listePlace[idplace]
        
    def afficheParkingGarentie(self):
        for i in self.ParckGarentie:
          print(i.voiture.immatirculation)

            
       

        
            





        
        