from abc import ABC,abstractmethod
class vehical(ABC):#abstrctclass
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class Bike(vehical):
    color = None
    def start(self):
     print(" lets start your ride... ")
     return self
    def stop(self):
     print(" stop your ride ... ")

class Car(vehical):
    color = None
    def start(self):
     print(" lets start your ride... ")
     return self
    def stop(self):
     print(" stop your ride ...  ")
