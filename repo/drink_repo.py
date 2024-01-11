
from models.drink import Drink
import pickle

class Drink_repo:
    def __init__(self):
        self.file='Drinks.data'
        self.drinks=[]

    def save(self):
        f = open(self.file, 'ab')
        pickle.dump(self.drinks, f)
        f.close()
    def add_drink(self,drink):
        self.drinks.append(drink)
        self.save()

    def read_drinks_list(self):
        f = open(self.file, 'rb')
        while True:
            try:
                x = pickle.load(f)
                self.drinks.append(x)
            except EOFError:
                break
        f.close()
        return self.drinks

    def delete_drink(self,drink:Drink):
        drinks_list = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    drinks_list.append(obj)
                except EOFError:
                    break

        for c in drinks_list:
                if c[0] == drink:
                    drinks_list.remove(c)
        f = open(self.file, 'wb')
        for k in drinks_list:
            pickle.dump(k, f)
        f.close()

    def find_drink(self, selected_drink):
        getranke = self.read_drinks_list() # [[],[],[]]
        found_drink = list(filter(lambda drink:  selected_drink.id == drink[0].id,getranke))
        if found_drink:
            return found_drink[0]
        else:
            return 'Drink does not exist!'

