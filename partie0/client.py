import pydoc
from voiture import Voiture

class Client:
    """
    Classe Client représentant un client d'un parking, pouvant être abonné ou super abonné.

    Attributes:
        estAbonne (bool): Indique si le client est abonné.
        estSuperAbonne (bool): Indique si le client est un super abonné.
        voiture (Voiture): Objet représentant la voiture du client (None par défaut).
        nom (str): Nom du client.
        adresse (str): Adresse du client.
        mp (str): Mode de paiement du client.
    """

    def __init__(self, nom, adresse, modeP):
        """
        Initialise un client avec son nom, son adresse et son mode de paiement.

        Args:
            nom (str): Nom du client.
            adresse (str): Adresse du client.
            modeP (str): Mode de paiement du client.
        """
        self.estAbonne = False
        self.estSuperAbonne = False
        self.voiture = None
        self.nom = nom
        self.adresse = adresse
        self.mp = modeP

    def nouvellevoiture(self, voiture):
        """
        Associe une nouvelle voiture au client.

        Args:
            voiture (Voiture): L'objet Voiture à associer au client.
        """
        pass

    def isAbonne(self):
        """
        Vérifie si le client est abonné.

        Returns:
            bool: True si le client est abonné, False sinon.
        """
        pass    

    def isSuperAbonne(self):
        """
        Vérifie si le client est un super abonné.

        Returns:
            bool: True si le client est un super abonné, False sinon.
        """
        pass
    
    def setAbonne(self, abonnement):
        """
        Définit le statut d'abonnement du client.

        Args:
            abonnement (bool): État d'abonnement à définir (True pour abonné, False pour désabonner).
        """
        pass

    def setSuperAbonne(self, abonnement):
        """
        Définit le statut de super abonnement du client.

        Args:
            abonnement (bool): État de super abonnement à définir (True pour super abonné, False pour désabonner).
        """
        pass

    def Desabonner(self, abonnement):
        """
        Désabonne le client, en modifiant son statut d'abonnement.

        Args:
            abonnement (bool): État d'abonnement à définir.
        """
        pass

    def demanderMaintenance(self):
        """
        Permet au client de demander une maintenance pour sa voiture.
        """
        pass

    def demanderLivraison(self, dateLivraison, heure, adresseLiv):
        """
        Permet au client de demander la livraison d'une voiture.

        Args:
            dateLivraison (str): Date de livraison souhaitée.
            heure (str): Heure de livraison souhaitée.
            adresseLiv (str): Adresse de livraison souhaitée.
        """
        pass 

    def sortirParking(self, parking, ticket):
        """
        Permet au client de sortir du parking en utilisant un ticket.

        Args:
            parking (object): Objet représentant le parking.
            ticket (object): Objet représentant le ticket de sortie.
        """
        pass

    def EntrerParking(self, parking):
        """
        Permet au client d'entrer dans le parking.

        Args:
            parking (object): Objet représentant le parking.
        """
        pass

    def affiche(self):
        """
        Affiche les informations du client.
        """
        pass

pydoc.writedoc("client")