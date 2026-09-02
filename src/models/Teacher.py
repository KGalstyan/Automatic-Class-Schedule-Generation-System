from __future__ import annotations

from src.models.logger import log_event


class Teacher:
    id: int
    subjects: list[Subject]
    available_slots: list[TimeSlot]

    def _log(self, message):
        log_event(f"Teacher: {message}")

    # Constructor
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        self.subjects = []
        self.available_slots = []
        self._log(f"initialized: id={self.id}, name={self.name}, surname={self.surname}")

    # Getters
    def get_id(self):
        self._log(f"get_id called -> {self.id}")
        return self.id

    def get_name(self):
        self._log(f"get_name called -> {self.name}")
        return self.name

    def get_surname(self):
        self._log(f"get_surname called -> {self.surname}")
        return self.surname

    def get_full_name(self):
        full_name = f"{self.name} {self.surname}"
        self._log(f"get_full_name called -> {full_name}")
        return full_name

    def get_available_slots(self):
        self._log(f"get_available_slots called -> {self.available_slots}")
        return self.available_slots

    def get_subjects(self):
        self._log(f"get_subjects called -> {self.subjects}")
        return self.subjects

    # Setters
    def set_name_surname(self, name, surname):
        self.name = name
        self.surname = surname
        self._log(f"set_name_surname called -> name={self.name}, surname={self.surname}")

    def set_subject(self, subject):
        self.subjects.append(subject)
        self._log(f"set_subject called -> subject={subject}, all_subjects={self.subjects}")

    def set_available_slots(self, a_slote):
        self.available_slots.append(a_slote)
        self._log(f"set_available_slots called -> slot={a_slote}, all_slots={self.available_slots}")

    # Methods
    def remove_subject(self, subject):
        self.subjects.remove(subject)
        self._log(f"remove_subject called -> subject={subject}, remaining_subjects={self.subjects}")

    def remove_available_slot(self, slot):
        self.available_slots.remove(slot)
        self._log(f"remove_available_slot called -> slot={slot}, remaining_slots={self.available_slots}")