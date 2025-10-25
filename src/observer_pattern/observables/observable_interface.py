from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observer_pattern.observers.observer_interface import IObserver


class IObservable(ABC):
    @abstractmethod
    def add_observer(self, observer: "IObserver") -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: "IObserver") -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass
