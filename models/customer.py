from models.identifiable import Identifiable

class Customer(Identifiable):
    def __init__(self,id,name,address):
        super().__init__(id)
        self.name=name
        self.address=address

    def __str__(self):
        return f'Customer({self.id},{self.name},{self.address})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id==other.id and self.name==other.name and self.address==other.address