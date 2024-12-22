from parking import Parking
from place import Place
from client import Client
from camera import Camera
from voiture import Voiture
from borneTicket import BorneTicket
from acces import Acces
from teleporteur import Teleporteur



Par = Parking(4, 4)
acces = Acces()
telepoteur = Teleporteur()
borneTicket = BorneTicket()

acces.actionneauPanneau()

c1 = Client('Assadick', '31100, Toulouse', 'CB')
voiture = Voiture(2, 3, "EF-441-TX")
c1.nouvellevoiture(voiture)


c2 = Client('Abdelrahim', '31100, Toulouse', 'CB')
voiture1 = Voiture(2, 3, "EF-442-TX")
c2.nouvellevoiture(voiture1)


#c2 = Client()
#voiture2 = Voiture(2, 3, "ET-442-TX")
#c2.nouvellevoiture(voiture2)



voiture1 = acces.actionnerCamera(c1)
idplace = c1.EntrerParking(Par)
telepoteur.teleporterVoiture(voiture1, Par.getPlace(idplace))
telepoteur.teleporterVoitureSuperAbonne(voiture1)
ticket = borneTicket.delivrerTicket(c1, idplace)
borneTicket.affichieTicket(ticket)


voiture3 = acces.actionnerCamera(c1)
idplace1 = c2.EntrerParking(Par)
telepoteur.teleporterVoiture(voiture3, Par.getPlace(idplace1))
telepoteur.teleporterVoitureSuperAbonne(voiture3)
ticket1 = borneTicket.delivrerTicket(c2, idplace1)
borneTicket.affichieTicket(ticket1)

#voiture2 = camera1.actionnerCamera(c2)
#place1 = Par.attribuerPlace(c2)

print("Places disponnibles dans le parking")
Par.affichePlaceDisponnible()

c1.sortirParking(Par, ticket)
print("Places disponnibles dans le parking")
Par.affichePlaceDisponnible()


#camera1 = Camera()
#voiture1 = camera1.actionnerCamera(c1)
#Par.attribuerPlace(c1)



