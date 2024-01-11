import pickle


from models.customer import Customer

class Customer_repo:
    def __init__(self):
        self.file='Customers.data'
        self.customers=[]

    def save(self):
        f = open(self.file, 'ab')
        pickle.dump(self.customers, f)
        f.close()
    def add_customer(self,customer:Customer):
        self.customers.append(customer)
        self.save()

    def read_customer_list(self):
        f=open(self.file,'rb')
        while True:
            try:
                x=pickle.load(f)
                self.customers.append(x)
            except EOFError:
                break
        f.close()
        return self.customers

    def update_customer(self,new_id,new_name,new_address,customer_to_update:Customer):
        lista=[]
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    lista.append(obj[0])
                except EOFError:
                    break

        if customer_to_update in lista:
            new_customer=Customer(new_id,new_name,new_address)
            index=lista.index(customer_to_update)
            lista[index]=new_customer

        f = open(self.file, 'wb')
        for i in lista:
            pickle.dump(i, f)
        f.close()

    def delete_customer(self,customer:Customer):
        kunden = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    kunden.append(obj)
                except EOFError:
                    break

        for c in kunden:
            if c == [customer]:
                kunden.remove(c)
        f = open(self.file, 'wb')
        for k in kunden:
            pickle.dump(k, f)
        f.close()

    def find_customer(self, selected_customer):
        customers = self.read_customer_list() # [[],[],[]]
        found_customer = list(filter(lambda customers:  selected_customer.id == customers[0].id and selected_customer.name==customers[0].name and selected_customer.address==customers[0].address,customers))
        if found_customer:
            return found_customer
