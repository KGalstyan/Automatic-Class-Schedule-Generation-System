from __future__ import annotations

from src.models.logger import log_event


class Schedule:

    def _log(self, message):
        log_event(f"Schedule: {message}")

    #Constructor
    def __init__(self, week):
        self.week = week
        self.lessons: list[Lesson] = []
        self._log(f"initialized: week={self.week}")

    #Getters
    def get_week(self):
        self._log(f"get_week called -> {self.week}")
        return self.week

    def get_lessons(self):
        self._log(f"get_lessons called -> {self.lessons}")
        return self.lessons

    #Setters
    def set_week(self, week):
        self.week = week
        self._log(f"set_week called -> {self.week}")

    def set_lessons(self, lesson):
        self.lessons.append(lesson)
        self._log(f"set_lessons called -> lesson={lesson}, all_lessons={self.lessons}")

    #methods
    def add_Lesson(self, lesson):
        self.lessons.append(lesson)
        self._log(f"add_Lesson called -> lesson={lesson}, all_lessons={self.lessons}")

    def get_by_group(self, group):
        result = [lesson for lesson in self.lessons if lesson.get_group() == group]
        self._log(f"get_by_group called -> group={group}, result={result}")
        return result

    def get_by_teacher(self, teacher):
        result = [lesson for lesson in self.lessons if lesson.get_teacher() == teacher]
        self._log(f"get_by_teacher called -> teacher={teacher}, result={result}")
        return result

    def get_by_room(self, room):
        result = [lesson for lesson in self.lessons if lesson.get_room() == room]
        self._log(f"get_by_room called -> room={room}, result={result}")
        return result

    def to_dict(self):
        result = {
            "week": self.week,
            "lessons": [lesson.to_dict() for lesson in self.lessons]
        }
        self._log(f"to_dict called -> {result}")
        return result