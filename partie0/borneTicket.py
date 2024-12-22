import pydoc
class BorneTicket:
    """
    Classe BorneTicket pour gérer la délivrance de tickets aux clients.

    Attributes:
        nbreTicket (int): Compteur du nombre total de tickets délivrés (variable de classe partagée par toutes les instances).

    Methods:
        delivrerTicket(client, idplace): Délivre un ticket à un client pour une place spécifique.
    """
    nbreTicket = 0  # Variable de classe pour suivre le nombre total de tickets émis

    def __init__(self):
        """
        Initialise une instance de BorneTicket et incrémente le compteur de tickets délivrés.
        """
        BorneTicket.nbreTicket += 1

    def delivrerTicket(self, client, idplace):
        """
        Délivre un ticket à un client pour une place spécifique.

        Args:
            client (object): Objet représentant le client à qui le ticket est délivré.
            idplace (int): Identifiant de la place attribuée au client.
        """
        pass
pydoc.writedoc("borneTicket")