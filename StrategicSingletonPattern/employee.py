from abc import ABC,abstractmethod
# Another exemple of subclasses
class Employee(ABC):
    
    def __init__(self,rank=None):
        self.currentcall = None
        self._rank = rank
    
    def isfree(self):
        return self.currentcall == None

class Director(Employee):

    def rankdirector(self):
        self._rank = 2
class Manager(Employee):
    
    def rankmanager(self):
        self._rank = 1

class Respondent(Employee):
    def rankrespondent(self):
        self._rank = 0


    


