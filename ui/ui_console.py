from repo.customer_repo import Customer_repo
from models.customer import Customer
from repo.gekochtergerichter_repo import Gekochtergerichter_repo
from models.gekochterGericht import GekochterGericht
from models.drink import Drink
from repo.drink_repo import Drink_repo
from repo.order_repo import Order_repo
class Console:
    def __init__(self):
        pass

    def menu(self):
        return """
        Choose option:
        1-customer
        2-menu options
        3-order
        4-exit
        """

    def customermenu(self): #opt1
        return"""
        Customer menu:
        1-add customer
        2-del customer
        3-view customers
        4-update a customer
        5-find a customer
        6-exit
        """

    def menuoptions(self): #opt2
        return"""
        menu options:
        1-food
        2-drink
        3-exit
        """

    def ordermenu(self): #opt3
        return"""
        Order menu:
        1-add food to order
        2-delete food from order
        3-add drink to order
        4-delete drink from order
        5-show order so far
        6-calculate total
        7-generate bill
        8-print bill
        9-exit
        """
    def foodmenu(self):
        return"""
        Food menu:
        1-add dish
        2-view avalibale dishes
        3-delete dish
        4-find dish
        5-exit
        """
    def drinkmenu(self):
        return """
        1-add drink
        2-view avalibale drinks
        3-delete drink
        4-find drink
        5-exit
        """

    def run(self):
        orderrepo = Order_repo()
        while True:
            print(self.menu())
            opt=int(input('Option:'))
            if opt==1:
                while True:
                    print(self.customermenu())
                    opt1=int(input('Option:'))
                    if opt1==1:
                        id1=int(input('Customer id: '))
                        nume1=str(input('Customer name: '))
                        address1=str(input('Customer address: '))
                        customer=Customer(id1,nume1,address1)
                        customerrepo=Customer_repo()
                        customerrepo.add_customer(customer)
                        print('Customer added')
                        break
                    if opt1==2:
                        id2=int(input('Id of Customer to delete: '))
                        name2=str(input('Name of Customer to delete: '))
                        address2=str(input('Address of the customer to delete: '))
                        customer2=Customer(id2,name2,address2)
                        customerrepo1=Customer_repo()
                        customerrepo1.delete_customer(customer2)
                        print('Customer deleted')
                        break
                    if opt1==3:
                        customerrepo3=Customer_repo()
                        print('Customers: ',customerrepo3.read_customer_list())
                        break
                    if opt1==4:
                        id4=int(input('Old id: '))
                        name4=str(input('Old name: '))
                        address4=str(input('Old address: '))
                        customer4=Customer(id4,name4,address4)
                        new_id=int(input('new id: '))
                        new_name=str(input('new name: '))
                        new_address=str(input('new address: '))
                        customerrepo4=Customer_repo()
                        customerrepo4.update_customer(new_id,new_name,new_address,customer4)
                        print('Customer updated')
                        break
                    if opt1==5:
                        id5 = int(input('Customer id: '))
                        name5 = str(input('Customer name: '))
                        address5 = str(input('Customer address: '))
                        customer5 = Customer(id5, name5, address5)
                        customerrepo5=Customer_repo()
                        print(customerrepo5.find_customer(customer5))
                        break

                    if opt1==6:
                        break



            if opt==2:
                while True:
                    print(self.menuoptions())
                    opt2=int(input('Option:'))
                    if opt2==1:
                        while True:
                            print(self.foodmenu())
                            opt4=int(input('Option:'))
                            if opt4==1:#add
                                name1=str(input('add food name: '))
                                id1=int(input('add food id: '))
                                portion1=int(input('add food portion: '))
                                price1=int(input('add food price: '))
                                preptime1=int(input('add food preptime: '))
                                food=GekochterGericht(name1,id1,portion1,price1,preptime1)
                                gekochtergerichtrepo=Gekochtergerichter_repo()
                                gekochtergerichtrepo.add(food)
                                print('Food added')
                                break
                            if opt4==3:#delete
                                name4=str(input('add food name: '))
                                id4 = int(input('add food id: '))
                                portion4 = int(input('add food portion: '))
                                price4 = int(input('add food price: '))
                                preptime4 = int(input('add food preptime: '))

                                food4 = GekochterGericht(name4,id4, portion4, price4, preptime4)
                                gekochtergerichtrepo4=Gekochtergerichter_repo()
                                gekochtergerichtrepo4.delete_food(food4)
                                print('food deleted')
                                break
                            if opt4==2:#view
                                foodrepo2=Gekochtergerichter_repo()
                                print(foodrepo2.load())
                                break

                            if opt4==4:#find
                                name3 = str(input('add food name: '))
                                id3 = int(input('add food id: '))
                                portion3 = int(input('add food portion: '))
                                price3 = int(input('add food price: '))
                                preptime3 = int(input('add food preptime: '))
                                food3=GekochterGericht(name3,id3,portion3,price3,preptime3)
                                foodrepo3=Gekochtergerichter_repo()
                                print(foodrepo3.find_dish(food3))
                                break
                            if opt4==5:
                                break
                    if opt2==2:
                        while True:
                            print(self.drinkmenu())
                            opt5=int(input('Option:'))
                            if opt5==1:

                                name1=str(input('add drink name: '))
                                id1=int(input('add drink id: '))
                                portion1 = int(input('add drink portion: '))
                                price1=int(input('add drink price: '))
                                alccontent1=int(input('add drink alcoholcontent: '))

                                drink1=Drink(name1,id1,portion1,price1,alccontent1)
                                drinkrepo1=Drink_repo()
                                drinkrepo1.add_drink(drink1)
                                print('Drink added')
                                break
                            if opt5==2:
                                drinkrepo4=Drink_repo()
                                print(drinkrepo4.read_drinks_list())
                                break
                            if opt5==3:
                                name3 = str(input('add drink name: '))
                                id3 = int(input('add drink id: '))
                                portion3 = int(input('add drink portion: '))
                                price3 = int(input('add drink price: '))
                                alccontent3 = int(input('add drink alcoholcontent: '))

                                drink3 = Drink(name3,id3, portion3, price3, alccontent3)
                                drinkrepo3=Drink_repo()
                                drinkrepo3.delete_drink(drink3)
                                print('Drink deleted')
                                break

                            if opt5==4:
                                name2 = str(input('add drink name: '))
                                id2 = int(input('add drink id: '))
                                portion2 = int(input('add drink portion: '))
                                price2 = int(input('add drink price: '))
                                alccontent2 = int(input('add drink alcoholcontent: '))

                                drink2 = Drink(name2,id2, portion2, price2, alccontent2)
                                drinkrepo2=Drink_repo()
                                print(drinkrepo2.find_drink(drink2))
                                break
                            if opt5==5:
                                break
                    if opt2==3:
                        break

            if opt==3:
                while True:
                    print(self.ordermenu())
                    opt3=int(input('Option:'))
                    if opt3==1:#add food
                        name=str(input('Name of the dish: '))
                        id=int(input('id of the dish: '))
                        portion=int(input('portion of the dish: '))
                        price=int(input('price of the dish: '))
                        preptime=int(input('preptime of the dish: '))
                        food=GekochterGericht(name,id,portion,price,preptime)
                        foodlist=[food]
                        foodrepo=Gekochtergerichter_repo()
                        ret=foodrepo.find_dish(food)
                        if type(ret) is str:
                            print('Dish does not exist!')
                            break
                        else:
                            orderrepo.add_food(foodlist)
                            print('Dish added to order!')
                            break
                    if opt3==2:#del food
                        name1 = str(input('Name of the dish: '))
                        id1 = int(input('id of the dish: '))
                        portion1 = int(input('portion of the dish: '))
                        price1 = int(input('price of the dish: '))
                        preptime1= int(input('preptime of the dish: '))
                        food1 = GekochterGericht(name1, id1, portion1, price1, preptime1)
                        foodlist1=[food1]
                        orderrepo.delete_food(foodlist1)
                        print('Food deleted!')
                        break
                    if opt3==3:#add drink
                        name = str(input('Name of the drink: '))
                        id = int(input('id of the drink: '))
                        portion = int(input('portion of the drink: '))
                        price = int(input('price of the drink: '))
                        alcoholcontent = int(input('alcoholcontent of the drink: '))
                        drink = Drink(name, id, portion, price, alcoholcontent)
                        drinklist=[drink]
                        drinkrepo = Drink_repo().find_drink(drink)
                        if type(drinkrepo) is str:
                            print('Drink does not exist!')
                            break
                        else:
                            orderrepo.add_drink(drinklist)
                            print('Drink added to order!')
                            break
                    if opt3==4:#del drink
                        name1 = str(input('Name of the drink: '))
                        id1 = int(input('id of the drink: '))
                        portion1 = int(input('portion of the drink: '))
                        price1 = int(input('price of the drink: '))
                        alcoholcontent1 = int(input('alcoholcontent of the drink: '))
                        drink1=Drink(name1, id1, portion1, price1, alcoholcontent1)
                        drinklist1=[drink1]
                        orderrepo.delete_drink(drinklist1)
                        print('Drink deleted!')
                        break
                    if opt3==5:
                        print(orderrepo.order_so_far())
                        break
                    if opt3==6:#cost
                        cost=orderrepo.cost_of_order()
                        print(f'The cost of the order is {cost}')
                        break
                    if opt3==7:
                        print(orderrepo.bill_gen())
                        print('Bill has been generated!')
                        break
                    if opt3==8:
                        print(orderrepo.bill_print())
                        break
                    if opt3==9:
                        break

            if opt==4:
                break

