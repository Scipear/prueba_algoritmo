class Teacher():
    def __init__(self, id: int, name: str, availabilities: list[Availability]):
        self.id = id
        self.name = name
        self.availabilities = availabilities

class Subject():
    def __init__(self, id: int, name: str, hours: int, teachers: list[Teacher]):
        self.id = id
        self.name = name
        self.hours = hours
        self.teachers = teachers

class Academic_Hour():
    def __init__(self, id: int, day: str, start_hour: str, end_hour: str):
        self.id = id
        self.day = day
        self.start_hour = start_hour
        self.end_hour = end_hour

class Room():
    def __init__(self, id:int, name: str):
        self.id = id
        self.name = name

class Group():
    def __init__(self, id: int, name: str, subjects: list[Subject]):
        self.id = id
        self.name = name
        self.subjects = subjects

class Availability():
    def __init__(self, id: int, start_hour: int, end_hour: int):
        self.id = id
        self.start_hour = start_hour
        self.end_hour = end_hour

class Event():
    def __init__(self, id: int, teacher: Teacher, subject: Subject, group: Group, duration: int):
        self.id = id
        self.group = group.id
        self.teacher = teacher.id
        self.subject = subject.id
        self.duration = duration
        self.start_hour = None
        self.room = None
    
    def __repr__(self):
        return f"(g {self.group} | s {self.subject} | t {self.teacher} | d {self.duration}h | s_h {self.start_hour} | e_h {(self.start_hour + self.duration) - 1} | r {self.room})"