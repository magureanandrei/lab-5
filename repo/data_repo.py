from abc import ABC,abstractmethod
import pickle

class Data_repo(ABC):
    def __init__(self,file):
        self.file=file
        self.list=[]

    def save(self):
        f = open(self.file, 'ab')
        pickle.dump(self.list, f)
        f.close()

    def load(self):
        f = open(self.file, 'rb')
        self.list = pickle.load(f)
        f.close()
        return self.list

    def read_file(self):
        f= open(self.file, 'r')
        for line in self.file:
            for el in line.split().strip():
                print(el)
        f.close()

    def write_to_file(self):
        f= open(self.file , 'wb')
        i=int(input('write something in a file: '))
        #f.write(f'{i}')
        f.close()

    # @abstractmethod
    # def convert_to_string(self, list):
    #     result = map(lambda x: str(x), list)
    #     joined_elements = ','.join(result)
    #     f = open(self.file, 'w')
    #     f.write(joined_elements)
    #     f.close()

    # @abstractmethod
    # def convert_from_string(self): # uses map function
    #     pass
