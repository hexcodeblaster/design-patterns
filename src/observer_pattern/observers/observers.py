from typing import override

from observer_pattern.observers.observer_interface import IObserver
from observer_pattern.observables.observable_interface import IObservable
from observer_pattern.observables.subjects.timed_reminder import Subject


class TimeObserver(IObserver):
    def subscribe_to_observable(self, observable: IObservable) -> None:
        observable.add_observer(self)

    def unsubscribe_from_observable(self, observable: IObservable) -> None:
        observable.remove_observer(self)

    @override
    def update(self, notified_from: IObservable) -> None:
        if isinstance(notified_from, Subject):
            hour = notified_from.hour
            minutes = notified_from.minute
            seconds = notified_from.second
            return_string = f"Current time is {hour}:{minutes}:{seconds}"
            print(return_string)
        return None

class DayObserver(IObserver):
    def subscribe_to_observable(self, observable: IObservable) -> None:
        observable.add_observer(self)

    def unsubscribe_from_observable(self, observable: IObservable) -> None:
        observable.remove_observer(self)

    @override
    def update(self, notified_from: IObservable) -> None:
        if isinstance(notified_from, Subject):
            day = notified_from.day
            month = notified_from.month
            year = notified_from.year
            return_string = f"Current date is {day}:{month}:{year}"
            print(return_string)
        return None
