from src.models.StudentGroup import StudentGroup
from src.models.logger import log_event
from src.models.Teacher import Teacher


class Subject:
    group: StudentGroup
    teacher: Teacher
    weekly_hours: int

    def _log(self, message):
        log_event(f"Subject: {message}")
    
    #Constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.group = None
        self.teacher = None
        self.weekly_hours = 0

    #Setters
    def set_group(self, group: StudentGroup):
        self.group = group
        self._log(f"set_group called -> group={self.group}")

    def set_teacher(self, teacher: Teacher):
        self.teacher = teacher
        self._log(f"set_teacher called -> teacher={self.teacher}")

    def set_weekly_hours(self, weekly_hours: int):
        self.weekly_hours = weekly_hours
        self._log(f"set_weekly_hours called -> weekly_hours={self.weekly_hours}")

    #Getters
    def get_id(self):
        self._log(f"get_id called -> {self.id}")
        return self.id

    def get_name(self):
        self._log(f"get_name called -> {self.name}")
        return self.name

    def get_group(self):
        self._log(f"get_group called -> {self.group}")
        return self.group

    def get_teacher(self):
        self._log(f"get_teacher called -> {self.teacher}")
        return self.teacher

    def get_weekly_hours(self):
        self._log(f"get_weekly_hours called -> {self.weekly_hours}")
        return self.weekly_hours