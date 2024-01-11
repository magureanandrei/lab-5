from models.court import Court

class GekochterGericht(Court):
    def __init__(self,name,id,portion,price,preptime):
        self.name=name
        super().__init__(id,portion,price)
        self.preptime=preptime


    def __str__(self):
        return f'Gericht({self.name},{self.id},{self.portion},{self.price},{self.preptime})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name==other.name and self.id==other.id and self.portion==other.portion and self.price==other.price and self.preptime==other.preptime


