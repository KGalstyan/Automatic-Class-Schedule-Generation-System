from src.models.logger import log_event


class StudentGroup:
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size
        log_event(f"StudentGroup: initialized: id={self.id}, name={self.name}, size={self.size}")
