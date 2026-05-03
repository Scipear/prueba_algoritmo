class Teacher():
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Subject():
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

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

class Chromosome():
    def __init__(self, teacher: Teacher, subject: Subject, academic_hour: Academic_Hour, room: Room, group: Group):
        self.teacher = teacher
        self.subject = subject
        self.academic_hour = academic_hour
        self.room = room
        self.group = group