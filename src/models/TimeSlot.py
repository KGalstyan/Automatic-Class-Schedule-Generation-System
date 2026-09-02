from src.models.logger import log_event


class TimeSlot:
    day: str
    start_time: str
    end_time: str

    def _log(self, message):
        log_event(f"TimeSlot: {message}")

    #Constructor
    def __init__(self, day, start_time, end_time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self._log(f"initialized: day={self.day}, start_time={self.start_time}, end_time={self.end_time}")

    #Methods
    def overlaps(self, other):
        result = self.day == other.day and not (self.end_time <= other.start_time or self.start_time >= other.end_time)
        self._log(f"overlaps called -> other={other.day}, result={result}")
        return result

    def delete(self):
        self._log(f"delete called -> removing TimeSlot: day={self.day}, start_time={self.start_time}, end_time={self.end_time}")
        del self