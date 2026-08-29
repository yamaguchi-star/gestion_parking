from service import Service

class Maintenance(Service):

    def __init__(self, dateDemande, dateService, apport):
        super().__init__(dateDemande, dateService, apport)

    def effectuerMaintenance(self):
        return {
            "dateDemande" : self.dateDemande,
            "dateService" : self.dateService,
            "appport" : self.apport
        }
