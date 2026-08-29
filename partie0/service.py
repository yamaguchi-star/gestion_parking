import pydoc
class Service:
    """
    Représente un service demandé et fourni dans le cadre d'une gestion d'activités.

    Attributs:
        dateDemande (datetime): La date à laquelle la demande de service a été effectuée.
        dateService (datetime): La date prévue ou réelle de la prestation du service.
        apport (float): La valeur ou le bénéfice apporté par le service (par exemple, en termes financiers ou autre mesure pertinente).

    Méthodes:
        Aucun pour l'instant. La classe agit comme un conteneur de données (modèle) pour stocker les informations
        liées à un service.

    Exemple d'utilisation:
        service = Service(dateDemande=datetime(2024, 12, 1), 
                          dateService=datetime(2024, 12, 10), 
                          apport=150.0)
    """
    def __init__(self, dateDemande, dateService, apport):
        self.dateDemande = dateDemande
        self.dateService = dateService
        self.apport = apport


pydoc.writedoc("service")