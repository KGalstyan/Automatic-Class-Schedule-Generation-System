from src.models.logger import log_event


class Lesson:

    def _log(self, message):
        log_event(f"Lesson: {message}")

    #Constructor
    def __init__(self, group, subject, teacher, room, day: str, start_time: str, end_time: str):
        self.group = group
        self.subject = subject
        self.teacher = teacher
        self.room = room
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self._log(f"initialized: group={self.group}, subject={self.subject}, teacher={self.teacher}, room={self.room}, day={self.day}, start_time={self.start_time}, end_time={self.end_time}")

