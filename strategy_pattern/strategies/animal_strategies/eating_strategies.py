from abc import ABC, abstractmethod

class EatingStrategy(ABC):
    @abstractmethod
    def eat(self):
        pass

class Horse(EatingStrategy):
    def eat(self):
        print("Chewing grass")

class Lion(EatingStrategy):
    def eat(self):
        print("Eating meat")