import pytest
from disenio_a_la_gorra.T01E01.timeclasses import TimeDataclass, TimeError


def test_hour_grather_than_0():
    with pytest.raises(TimeError):
        hora_erronea = TimeDataclass.at(-1, 0, 0)

def test_hour_smaller_than_23():
    with pytest.raises(TimeError):
        hora_erronea = TimeDataclass.at(24, 0, 0)

def test_minute_grather_than_59():
    with pytest.raises(TimeError):
        minute_erronea = TimeDataclass.at(22, 60, 0)

def test_minute_smaller_than_0():
    with pytest.raises(TimeError):
        minute_erronea = TimeDataclass.at(22, -1, 0)

def test_second_grather_than_59():
    with pytest.raises(TimeError):
        second_erronea = TimeDataclass.at(22, 22, 60)

def test_second_smaller_than_0():
    with pytest.raises(TimeError):
        second_erronea = TimeDataclass.at(22, 22, -1)

def test_time_use_integer():
    with pytest.raises(TimeError):
        hour_erronea = TimeDataclass.at(0.1, 0, 0)
    with pytest.raises(TimeError):
        minute_erronea = TimeDataclass.at(0, 0.1, 0)
    with pytest.raises(TimeError):
        second_erronea = TimeDataclass.at(0, 0, -0.1)