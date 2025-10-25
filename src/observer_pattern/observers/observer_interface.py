from abc import ABC, abstractmethod
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from observer_pattern.observables.observable_interface import IObservable


class IObserver(ABC):
    @abstractmethod
    def update(self, notified_from: 'IObservable') -> Any:
        pass