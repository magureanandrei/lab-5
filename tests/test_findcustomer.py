from repo.customer_repo import Customer_repo
from models.customer import Customer

def test_customer():
    customer1=Customer(1,'Vasile Pop','str.idk nr.9')
    customer2=Customer(2,'Ioan Pop','str.21 Decembrie nr.78')
    customer_repo=Customer_repo()


    print(customer_repo.read_customer_list())
    customer_repo.delete_customer(customer1)
    customer_repo.delete_customer(customer2)
test_customer()
