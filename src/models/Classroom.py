from src.models.TimeSlot import TimeSlot
from src.models.logger import log_event


class Classroom:
    id: int
    capacity: int
    room_name: str
    busy_slots: list[TimeSlot]

    def _log(self, message):
        log_event(f"Classroom: {message}")

    #Constructor
    def __init__(self, id, capacity, room_name):
        self.id = id
        self.capacity = capacity
        self.room_name = room_name
        self.busy_slots = []
        self._log(f"initialized: id={self.id}, capacity={self.capacity}, room_name={self.room_name}")

    #Getters
    def get_id(self):
        self._log(f"get_id called -> {self.id}")
        return self.id

    def get_capacity(self):
        self._log(f"get_capacity called -> {self.capacity}")
        return self.capacity

    def get_room_name(self):
        self._log(f"get_room_name called -> {self.room_name}")
        return self.room_name

    def get_busy_slots(self):
        self._log(f"get_busy_slots called -> {self.busy_slots}")
        return self.busy_slots

    #Setters
    def set_id(self, id):
        self.id = id
        self._log(f"set_id called -> {self.id}")

    def set_capacity(self, capacity):
        self.capacity = capacity
        self._log(f"set_capacity called -> {self.capacity}")

    def set_room_name(self, room_name):
        self.room_name = room_name
        self._log(f"set_room_name called -> {self.room_name}")

    def set_busy_slots(self, busy_slot):
        self.busy_slots.append(busy_slot)
        self._log(f"set_busy_slots called -> slot={busy_slot}, busy_slots={self.busy_slots}")

    #Methods
    def fits(self, group_size):
        result = self.capacity >= group_size
        self._log(f"fits called -> group_size={group_size}, result={result}")
        return result

    def is_available(self, day, start_time, end_time):
        for slot in self.busy_slots:
            if slot.day == day and not (end_time <= slot.start_time or start_time >= slot.end_time):
                self._log(f"is_available called -> day={day}, start_time={start_time}, end_time={end_time}, result=False")
                return False
        self._log(f"is_available called -> day={day}, start_time={start_time}, end_time={end_time}, result=True")
        return True