import pickle
from models.drink import Drink
from models.gekochterGericht import GekochterGericht
from repo.data_repo import Data_repo
import functools
from repo.gekochtergerichter_repo import Gekochtergerichter_repo
from repo.drink_repo import Drink_repo

class Order_repo(Data_repo):

    def __init__(self):
        self.orders=[]
        self.dishes=[]
        self.drinks=[]
        self.gesamtkosten=[]
        self.dishes=Gekochtergerichter_repo().load()
        self.drinks=Drink_repo().read_drinks_list()


    def add_food(self,food:list[GekochterGericht]):
        if food in self.dishes:
            print('intrat in if')
            print(food)
            self.orders.append(food)
            print(self.orders)
        else:
            print("This dish isn't in the menu!")

    # def add_food(self,food:GekochterGericht):
    #     self.dishes.append(food)
    #     self.save()

    def delete_food(self,food:[GekochterGericht]):
        if food in self.orders:
            self.orders.remove(food)
        else:
            print("This dish wasn't ordered!")

    def add_drink(self,drink:[Drink]):
        if drink in self.drinks:
            self.orders.append(drink)
        else:
            print("This drink isn't in the menu!")

    def delete_drink(self,drink:[Drink]):
        if drink in self.orders:
            self.orders.remove(drink)
        else:
            print("This dish wasn't ordered!")

    def order_so_far(self):
        return self.orders

    def cost_of_order(self):
        costs=[]
        for i in self.orders:
            i=i[0]
            a=i.price
            costs.append(a)
        self.gesamtkosten=functools.reduce(lambda x,y:x+y,costs)
        return self.gesamtkosten

    def bill_gen(self):
        bill_list=[]
        for i in self.orders:
            bill_list.append(i)
        return bill_list

    def bill_print(self):
        bill_list=self.bill_gen()
        bill=f''
        bill+=f'----------BILL----------\n'
        for i in bill_list:
            i=i[0]
            a=i.name
            b=i.price
            bill+=f'{a}..........{b}\n'
        bill+=f'TOTAL: {self.gesamtkosten}'
        return bill





