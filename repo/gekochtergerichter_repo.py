
from models.gekochterGericht import GekochterGericht
import pickle
class Gekochtergerichter_repo:
    def __init__(self):
        self.file='Food.data'
        self.gekochtergerichte=[]

    def save(self):
        f = open(self.file, 'ab')
        pickle.dump(self.gekochtergerichte, f)
        f.close()
    def add(self, neues_gericht):
        self.gekochtergerichte.append(neues_gericht)
        self.save()

    def delete_food(self,food:GekochterGericht):
        food_list = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    food_list.append(obj)
                except EOFError:
                    break
        for c in food_list:
                if c[0] == food:
                    food_list.remove(c)


        f = open(self.file, 'wb')
        for k in food_list:
            pickle.dump(k, f)
        f.close()
    def load(self):
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    self.gekochtergerichte.append(obj)
                except EOFError:
                    break
        return self.gekochtergerichte

    def find_dish(self, selected_food):
        gerichte = self.load()  # [[],[],[]]
        found_dish = list(filter(lambda drink: selected_food.id == drink[0].id, gerichte))
        if found_dish:
            return found_dish[0]
        else:
            return 'Dish does not exist!'