from strategy_pattern.strategies.animal_strategies.eating_strategies import (
    CarnivoreEatingStrategy,
    EatingStrategy,
    HerbivoreEatingStrategy,
    OmnivoreEatingStrategy,
)


class Animal:
    def __init__(self, eating_strategy: EatingStrategy) -> None:
        self.eating_strategy = eating_strategy

    def eat(self) -> None:
        self.eating_strategy.eat()


class Horse(Animal):
    def __init__(self) -> None:
        super().__init__(eating_strategy=HerbivoreEatingStrategy())


class Lion(Animal):
    def __init__(self):
        super().__init__(eating_strategy=CarnivoreEatingStrategy())


class Human(Animal):
    def __init__(self):
        super().__init__(eating_strategy=OmnivoreEatingStrategy())
