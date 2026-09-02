#!/usr/bin/env python3
import models.schedule as schedule
import models.lesson as lesson
import models.studentgroup as studentgroup
import models.subject as subject
import models.teacher as teacher
import models.classroom as classroom
import models.timeslot as timeslot

def main():
    # Create a schedule for week 1
    my_schedule = schedule.Schedule(week=1)

    # Create some student groups
    group1 = studentgroup.StudentGroup(id=1, name="Group 1", size=30)
    group2 = studentgroup.StudentGroup(id=2, name="Group 2", size=25)

    # Create some subjects
    math = subject.Subject(id=1, name="Math")
    physics = subject.Subject(id=2, name="Physics")

    # Create some teachers
    teacher1 = teacher.Teacher(id=1, name="John", surname="Doe")
    teacher2 = teacher.Teacher(id=2, name="Jane", surname="Smith")

    # Assign subjects to teachers
    teacher1.set_subject(math)
    teacher2.set_subject(physics)

    # Create some classrooms
    room101 = classroom.Classroom(id=1, capacity=40, room_name="Room 101")
    room102 = classroom.Classroom(id=2, capacity=30, room_name="Room 102")

    # Create some time slots
    slot1 = timeslot.TimeSlot(day="Monday", start_time="09:00", end_time="10:00")
    slot2 = timeslot.TimeSlot(day="Monday", start_time="10:00", end_time="11:00")

    # Add busy slots to classrooms
    room101.set_busy_slots(slot1)
    room102.set_busy_slots(slot2)