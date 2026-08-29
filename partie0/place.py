import pydoc
class Place:
    """
    Classe Place représentant une place de parking individuelle.

    Attributes:
        numero (int): Numéro unique de la place.
        niveau (int): Niveau du parking où se situe la place.
        longueur (float): Longueur de la place en mètres.
        hauteur (float): Hauteur de la place en mètres.
        disponible (bool): Indique si la place est actuellement disponible (True par défaut).
        pourSuperAbonne (bool): Indique si la place est réservée pour les super abonnés (False par défaut).
    """

    def __init__(self, numero, niveau, longueur, hauteur):
        """
        Initialise une place de parking avec un numéro, un niveau et des dimensions.

        Args:
            numero (int): Numéro unique de la place.
            niveau (int): Niveau du parking où se situe la place.
            longueur (float): Longueur de la place en mètres.
            hauteur (float): Hauteur de la place en mètres.
        """
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur
        self.hauteur = hauteur
        self.disponnible = True
        self.pourSuperAbonne = False

    def estDisponible(self):
        """
        Vérifie si la place est disponible.

        Returns:
            bool: True si la place est disponible, False sinon.
        """
        pass

    def setEstDisponible(self, disponible):
        """
        Définit l'état de disponibilité de la place.

        Args:
            disponible (bool): Nouvel état de disponibilité de la place.
        """
        pass

    def estPourSuperAbonne(self):
        """
        Vérifie si la place est réservée pour les super abonnés.

        Returns:
            bool: True si la place est réservée pour les super abonnés, False sinon.
        """
        pass

    def setEstPourSuperAbonne(self, pourSuperAbonne):
        """
        Définit si la place est réservée pour les super abonnés.

        Args:
            pourSuperAbonne (bool): Nouvel état de réservation pour super abonnés.
        """
        pass

pydoc.writedoc("place")