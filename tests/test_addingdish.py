from models.gekochterGericht import GekochterGericht
from repo.gekochtergerichter_repo import Gekochtergerichter_repo

def test_addingfood():
    food=GekochterGericht('orez',2,200,20,20)
    foodrepo=Gekochtergerichter_repo()
    foodrepo.add(food)
    print(foodrepo.load())

test_addingfood()
