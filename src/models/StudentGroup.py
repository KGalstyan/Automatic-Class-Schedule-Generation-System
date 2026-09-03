from src.models.logger import log_event

class StudentGroup:
    subjects: list[Subject]
    busy_slots: list[TimeSlot]

    def _log(self, message):
        log_event(f"StudentGroup: {message}")

    #Constructor
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size
        self._log(f"initialized: id={self.id}, name={self.name}, size={self.size}")

    #Getters
    def get_id(self):
        self._log(f"get_id called -> {self.id}")
        return self.id

    def get_name(self):
        self._log(f"get_name called -> {self.name}")
        return self.name

    def get_size(self):
        self._log(f"get_size called -> {self.size}")
        return self.size

    #Setters
    def set_name(self, name):
        self.name = name
        self._log(f"set_name called -> {self.name}")

    def set_size(self, size):
        self.size = size
        self._log(f"set_size called -> {self.size}")