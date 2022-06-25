
class TimeZone:
    def __init__(self, offset: int = 0, nombre: str = None):
        self.offset = offset
        self.nombre = nombre

    def normalized_hour(self, hour: int) -> int:
        return hour - self.offset
