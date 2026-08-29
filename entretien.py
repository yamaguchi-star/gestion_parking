from service import Service



class Entretien(Service):
    def __init__(self, dateDemande, dateService, apport):
        super().__init__(dateDemande, dateService, apport)


    def effectuerEntretien(self):
        return {
            "dateDemande" : self.dateDemande,
            "dateService" : self.dateService,
            "apport" : self.apport
        }