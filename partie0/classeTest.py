import unittest
from parking import Parking
from place import Place
from client import Client
from camera import Camera
from voiture import Voiture
from borneTicket import BorneTicket

class TestParkingSystem(unittest.TestCase):
    """
    Classe de tests unitaires pour le système de gestion de parking.
    """

    def setUp(self):
        """
        Méthode exécutée avant chaque test pour initialiser l'environnement de test.
        """
        self.parking = Parking(2, 10)  # 2 étages, 10 places par étage
        self.camera = Camera()
        self.borneTicket = BorneTicket()

        # Création d'un client et de sa voiture
        self.client1 = Client('Assadick', '31100, Toulouse', 'CB')
        self.voiture1 = Voiture(2, 3, "EF-441-TX")
        self.client1.nouvellevoiture(self.voiture1)

    def test_ajout_client_et_voiture(self):
        """
        Teste l'ajout d'une voiture pour un client.
        """
        self.assertEqual(self.client1.voiture, self.voiture1)
        self.assertEqual(self.client1.nom, 'Assadick')
        print("Test ajout client et voiture réussi.")

    def test_entree_parking(self):
        """
        Teste l'entrée d'un client dans le parking.
        """
        voiture_detectee = self.camera.actionnerCamera(self.client1)
        self.assertIsNotNone(voiture_detectee, "La voiture n'a pas été détectée par la caméra.")
        idplace = self.client1.EntrerParking(self.parking)
        self.assertIsNotNone(idplace, "Aucune place n'a été attribuée.")
        print(f"Test entrée parking réussi, place attribuée : {idplace}.")

    def test_generation_ticket(self):
        """
        Teste la génération d'un ticket pour une place attribuée.
        """
        idplace = self.client1.EntrerParking(self.parking)
        ticket = self.borneTicket.delivrerTicket(self.client1, idplace)
        self.assertIsNotNone(ticket, "Le ticket n'a pas été généré.")
        print("Test génération ticket réussi.")

    def test_sortie_parking(self):
        """
        Teste la sortie d'un client du parking.
        """
        idplace = self.client1.EntrerParking(self.parking)
        ticket = self.borneTicket.delivrerTicket(self.client1, idplace)
        self.client1.sortirParking(self.parking, ticket)
        self.assertTrue(self.client1.voiture.getEstDansParking() is False, "La voiture n'est pas sortie du parking.")
        print("Test sortie parking réussi.")

    def test_places_disponibles(self):
        """
        Teste l'affichage des places disponibles.
        """
        self.parking.affichePlaceDisponnible()
        self.assertGreater(self.parking.nbrePlacesLibre, 0, "Aucune place disponible dans le parking.")
        print("Test places disponibles réussi.")

    def tearDown(self):
        """
        Méthode exécutée après chaque test pour nettoyer l'environnement si nécessaire.
        """
        print("Nettoyage après le test.")

# Exécute les tests
if __name__ == '__main__':
    unittest.main()