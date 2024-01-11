from models.identifiable import Identifiable

class Court(Identifiable):
    def __init__(self,id,portion,price):
        super().__init__(id)
        self.portion=portion
        self.price=price
