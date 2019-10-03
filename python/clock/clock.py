class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        total_minutes = self.hour * 60 + self.minute
        repr_hour = int(total_minutes // 60) % 24
        repr_minute = total_minutes % 60
        return "{:02}:{:02}".format(repr_hour, repr_minute)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        self.minute = self.minute + minutes
        return self.__repr__()

    def __sub__(self, minutes):
        self.minute = self.minute - minutes
        return self.__repr__()
