from models.identifiable import Identifiable

class Order(Identifiable):
    def __init__(self,id,gesamtkosten):
        super().__init__(id)
        self.gesamtkosten=gesamtkosten

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass



