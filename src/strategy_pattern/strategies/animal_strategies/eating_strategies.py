from abc import ABC, abstractmethod


class EatingStrategy(ABC):
    @abstractmethod
    def eat(self) -> None:
        pass


class HerbivoreEatingStrategy(EatingStrategy):
    def eat(self) -> None:
        print("Eating salad")


class CarnivoreEatingStrategy(EatingStrategy):
    def eat(self) -> None:
        print("Eating meat")


class OmnivoreEatingStrategy(EatingStrategy):
    def eat(self) -> None:
        print("Eating salad with meat")
