from datetime import datetime
from unittest.mock import call

from observer_pattern.observables.subjects.timed_reminder import Subject
from observer_pattern.observers.observers import TimeObserver


def test_timed_observers_update(mocker):
    time_observer = TimeObserver()
    observable_subject = Subject({time_observer})
    mock_update = mocker.patch.object(time_observer, "update")
    now = datetime.now()
    observable_subject.hour = now.hour
    observable_subject.minute = now.minute
    observable_subject.second = now.second
    mock_update.assert_has_calls([call(observable_subject)] * 3)


def test_timed_observers_registration(mocker):
    time_observer = TimeObserver()
    observable_subject = Subject()
    mock_update = mocker.patch.object(time_observer, "update")

    observable_subject.notify_observers()
    mock_update.assert_not_called()

    observable_subject.add_observer(time_observer)

    observable_subject.notify_observers()
    mock_update.assert_called_once_with(observable_subject)


def test_timed_observers_deregistration(mocker):
    time_observer = TimeObserver()
    observable_subject = Subject()
    mock_update = mocker.patch.object(time_observer, "update")
    observable_subject.add_observer(time_observer)
    observable_subject.notify_observers()
    mock_update.assert_called_once_with(observable_subject)
    observable_subject.remove_observer(time_observer)
    mock_update.reset_mock()
    observable_subject.notify_observers()
    mock_update.assert_not_called()


def test_removing_absent_observer():
    time_observer = TimeObserver()
    observable_subject = Subject()
    observable_subject.remove_observer(time_observer)
