from .timezone import TimeZone
from dataclasses import dataclass, fields

class TimeError(Exception):
    """ Exception raised when hour, minute or second are out of range
        hour between 0 and 23
        minute between 0 and 59
        second between 0 and 59
    """

class TimeTypeError(Exception):
    """ Exception raised when hour, minute or second are not integer
    """

@dataclass(frozen=True)
class TimeDataclass:
    hour: int
    minute: int
    second: int
    timezone: TimeZone = TimeZone(0, 'UTC')

    @staticmethod
    def at(hour: int, minute: int, second: int) -> 'TimeDataclass':
        if not hour >= 0 or not hour <= 23 or type(hour) is not int:
            raise TimeError("La hora tiene ser un entero entre 0 y 23")
        if not minute >= 0 or not minute <= 59 or type(minute) is not int:
            raise TimeError("Los minutos tienen que ser un entero entre 0 y 59")
        if not second >= 0 or not second <= 59 or type(second) is not int:
            raise TimeError("Los segundos tienen que ser un entero entre 0 y 59")

        return TimeDataclass(hour, minute, second)


    def difference_in_hour(self, time_to_compare: 'TimeDataclass') -> int:
        return self._normalized_hour() - time_to_compare._normalized_hour()

    def _normalized_hour(self):
        return self.timezone.normalized_hour(self.hour)


class Time:
    def __init__(self, hour: int, minute: int, second: int, timezone: TimeZone = TimeZone(0, 'UTC')):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.timezone = timezone

    def difference_in_hour(self, time_to_compare: 'Time') -> int:
        return self._normalized_hour() - time_to_compare._normalized_hour()

    def _normalized_hour(self):
        return self.timezone.normalized_hour(self.hour)