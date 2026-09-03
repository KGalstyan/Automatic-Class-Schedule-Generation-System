#!/usr/bin/env python3
import os
import sys

from numpy import delete

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.models.Schedule import Schedule
from src.models.Lesson import Lesson
from src.models.StudentGroup import StudentGroup
from src.models.Subject import Subject
from src.models.Teacher import Teacher
from src.models.Classroom import Classroom
from src.models.TimeSlot import TimeSlot

def main():
    # Create a schedule for week 1
    my_schedule = Schedule(week=1)

    # Create some student groups
    group1 = StudentGroup(id=1, name="Group 1", size=30)
    group2 = StudentGroup(id=2, name="Group 2", size=25)
    group1.set_name("Advanced Group 1")
    group2.set_name("Advanced Group 2")
    group1.set_size(35)
    group2.set_size(28)
    

    print("Application started successfully.")
    print(f"Schedule week: {my_schedule.get_week()}")
    print(f"Teachers: {teacher1.get_full_name()}, {teacher2.get_full_name()}")
    return 0

if __name__ == "__main__":
    main()