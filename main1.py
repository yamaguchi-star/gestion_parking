from parking import Parking
from place import Place
from client import Client
from camera import Camera
from voiture import Voiture
from borneTicket import BorneTicket
from acces import Acces
from teleporteur import Teleporteur
import json

# Création du parking avec 10 étages et 10 places par étage
Par = Parking(10, 10)

# Initialisation des composants nécessaires pour la gestion du parking
acces = Acces()  # Gère l'accès au parking
telepoteur = Teleporteur()  # Déplace les voitures vers leurs places
borneTicket = BorneTicket()  # Gère la délivrance et l'affichage des tickets

# Chargement des données de test à partir d'un fichier JSON
with open("donnees.json", "r") as f:
    donneesTest = json.load(f)  # Les données contiennent des informations sur les clients et leurs voitures

# Initialisation des listes pour stocker les clients et leurs tickets
clients = list()
tickets = list()

# Parcours des données de test pour créer les clients et leurs voitures
for client in donneesTest:
    # Création d'un objet Client avec les données du fichier
    c = Client(
        client["client"]['nom'], 
        client["client"]['adresse'], 
        client["client"]['moyen_paiement'], 
        client["client"]['superabonne']
    )

    # Création d'un objet Voiture avec les dimensions et immatriculation
    v = Voiture(
        client['voiture']["hauteur"], 
        client['voiture']["longueur"], 
        client['voiture']["immatriculation"]
    )
    
    # Association de la voiture au client
    clients.append(c)
    c.nouvellevoiture(v)

    # Simulation de l'entrée de la voiture dans le parking
    voiture1 = acces.actionnerCamera(c)  # Détection de la voiture par la caméra
    idplace = c.EntrerParking(Par)  # Attribution d'une place dans le parking

    # Téléportation de la voiture vers la place attribuée
    telepoteur.teleporterVoiture(voiture1, Par.getPlace(idplace))
    
    # Délivrance d'un ticket pour le client et stockage dans la liste des tickets
    ticket = borneTicket.delivrerTicket(c, idplace)
    tickets.append(ticket)
    borneTicket.affichieTicket(ticket)  # Affichage du ticket délivré

# Affiche les places disponibles après le stationnement des voitures
Par.affichePlaceDisponnible()

# Section commentée pour gérer la sortie des clients (à compléter)
# for cl, ticket in zip(clients, tickets):
#     cl.sortirParking(Par, ticket)

print()

# Affiche les voitures garées dans le parking pour les super abonnés
print("Les voitures garées dans le ParkGarentie :")
Par.afficheParkingGarentie()