from datetime import datetime
from typing import override

from observer_pattern.observables.observable_interface import IObservable
from observer_pattern.observers.observer_interface import IObserver

class Subject(IObservable):
    def __init__(self, observer_list: list[IObserver] | None = None) -> None:
        self._observer_list = observer_list
        self._hour = datetime.now().hour
        self._minute = datetime.now().minute
        self._second = datetime.now().second
        self._day = datetime.now().day
        self._month = datetime.now().month
        self._year = datetime.now().year

    @override
    def add_observer(self, observer: IObserver) -> None:
        self._observer_list.append(observer)

    @override
    def remove_observer(self, observer: IObserver) -> None:
        self._observer_list.remove(observer)

    @override
    def notify_observers(self) -> None:
        for observer in self._observer_list:
            observer.update(self)

    def set_time(self):
        self._hour = datetime.hour
        self._minute = datetime.minute
        self._second = datetime.second
        self._day = datetime.day
        self._month = datetime.month
        self._year = datetime.year
        self.notify_observers()

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    @property
    def second(self) -> int:
        return self._second

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year
