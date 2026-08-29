import pydoc
class Camera:
    """
    Classe Camera pour capturer des informations spécifiques sur une voiture telles que
    sa longueur, sa hauteur et son immatriculation.

    Methods:
        capturerLongueur(voiture): Capture la longueur de la voiture.
        capturerHauteur(voiture): Capture la hauteur de la voiture.
        capturerImmatriculation(voiture): Capture le numéro d'immatriculation de la voiture.
    """

    def capturerLongueur(self, voiture):
        """
        Capture la longueur de la voiture.

        Args:
            voiture (object): Objet représentant la voiture dont on veut capturer la longueur.
        """
        pass

    def capturerHauteur(self, voiture):
        """
        Capture la hauteur de la voiture.

        Args:
            voiture (object): Objet représentant la voiture dont on veut capturer la hauteur.
        """
        pass

    def capturerImmatriculation(self, voiture):
        """
        Capture le numéro d'immatriculation de la voiture.

        Args:
            voiture (object): Objet représentant la voiture dont on veut capturer l'immatriculation.
        """
        pass

pydoc.writedoc("camera")