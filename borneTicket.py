

class BorneTicket:
    nbreTicket = 0
    def __init__(self):
        self.nbreTicket+=1

    def delivrerTicket(self, client, idplace):
        if idplace is not None:

            return {
                'numeroTicket':self.nbreTicket,
                'Nom': client.nom,
                'Adresse': client.adresse,
                'ima': client.voiture.immatirculation,
                'place':idplace,
                'MP' : client.mp
            }
    def affichieTicket(self, ticket):
        if ticket is not None:
            print("#------------------------------------------------#")
            print("|   Numero Ticket   : ", ticket['numeroTicket'])
            print("|   Nom Client      : ", ticket['Nom'])
            print("|   Adresse Client  : ", ticket['Adresse'])
            print("|   Immatirculation : ", ticket['ima'])
            print("|   Numero Place    : ", ticket['place'])
            print("#------------------------------------------------#")
