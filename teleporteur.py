class Teleporteur:
    def teleporterVoiture(self, voiture, place):
        if place is not None:
          print(f"Votre voiture d'immatirculation : {voiture.getImmatirculation()} est teleportée à la place : {place.numero}")


    def teleporterVoitureSuperAbonne(self, voiture):
        print("Votre place est teleportée à sa place habituelle")