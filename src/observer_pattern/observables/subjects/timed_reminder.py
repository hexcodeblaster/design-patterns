from datetime import datetime
from typing import override

from observer_pattern.observables.observable_interface import IObservable
from observer_pattern.observers.observer_interface import IObserver


class Subject(IObservable):
    def __init__(self, observers: set[IObserver] | None = None) -> None:
        self._observers = observers or set()
        self._hour = datetime.now().hour
        self._minute = datetime.now().minute
        self._second = datetime.now().second
        self._day = datetime.now().day
        self._month = datetime.now().month
        self._year = datetime.now().year

    @override
    def add_observer(self, observer: IObserver) -> None:
        self._observers.add(observer)

    @override
    def remove_observer(self, observer: IObserver) -> None:
        self._observers.discard(observer)

    @override
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self)

    @property
    def hour(self) -> int:
        return self._hour

    @hour.setter
    def hour(self, hour_val: int | None = None):
        self._hour = hour_val or datetime.now().hour
        self.notify_observers()

    @property
    def minute(self) -> int:
        return self._minute

    @minute.setter
    def minute(self, minute_val: int | None = None):
        self._minute = minute_val or datetime.now().minute
        self.notify_observers()

    @property
    def second(self) -> int:
        return self._second

    @second.setter
    def second(self, second_val: int | None = None):
        self._second = second_val or datetime.now().second
        self.notify_observers()

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, day_val: int | None = None):
        self._day = day_val or datetime.now().day
        self.notify_observers()

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, month_val: int | None = None):
        self._month = month_val or datetime.now().month
        self.notify_observers()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year_val: int | None = None):
        self._year = year_val or datetime.now().year
        self.notify_observers()
