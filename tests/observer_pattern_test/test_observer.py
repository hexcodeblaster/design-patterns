from datetime import datetime

from observer_pattern.observers.observers import TimeObserver, DayObserver
from observer_pattern.observables.subjects.timed_reminder import Subject

def test_timed_observers(capsys):
    time_observer = TimeObserver()
    observable_subject = Subject([time_observer])
    now = datetime.now()
    observable_subject.hour = (curr_hour := now.hour)
    observable_subject.minute = (curr_minute := now.minute)
    observable_subject.second = (curr_second := now.second)
    captured = capsys.readouterr()
    assert f"Current time is {curr_hour}:{curr_minute}:{curr_second}" == captured.out.split('\n')[0].strip()
    observable_subject.remove_observer(time_observer)

def test_date_observers(capsys):
    day_observer = DayObserver()
    observable_subject = Subject([day_observer])
    now = datetime.now()
    observable_subject.day = (curr_day := now.day)
    observable_subject.month = (curr_month := now.month)
    observable_subject.year = (curr_year := now.year)
    observable_subject.notify_observers()
    captured = capsys.readouterr()
    assert f"Current date is {curr_day}:{curr_month}:{curr_year}" == captured.out.split('\n')[0].strip()
    observable_subject.remove_observer(day_observer)
