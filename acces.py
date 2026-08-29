from voiture import Voiture
from camera import Camera
from panneau import PanneauAffichage
from parking import Parking
class Acces:
    def actionnerCamera(self, client):
        camera = Camera()
        return Voiture(camera.capturerHauteur(client.voiture), camera.caputurerLongueur(client.voiture), camera.capturerImmatirculation(client.voiture))


    def actionneauPanneau(self):
       paneau = PanneauAffichage()
       return paneau.afficherNbrePlaceDisponnible(Parking.get_instanceParking())
    

    
