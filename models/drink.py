from models.court import Court

class Drink(Court):
    def __init__(self,name,id,portion,price,alcoholcontent):
        self.name=name
        super().__init__(id,portion,price)
        self.alcoholcontent=alcoholcontent


    def __str__(self):
        return f'Drink({self.name},{self.id},{self.portion},{self.price},{self.alcoholcontent})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name==other.name and self.id==other.id and self.portion==other.portion and self.price==other.price and self.alcoholcontent==other.alcoholcontent
