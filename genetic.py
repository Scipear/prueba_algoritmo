import numpy as np
import random
from classes import Teacher, Subject, Academic_Hour, Room, Group

teachers = [
    Teacher(1, "Maria Lopez"),
    Teacher(2, "Juan Lopez"),
    Teacher(3, "Jose Lopez"),
    Teacher(4, "Roberta Lopez"),
    Teacher(5, "Luisa Lopez")
]

subjects = [
    Subject(1, "Matematica"),
    Subject(2, "Fisica"),
    Subject(3, "Quimica"),
    Subject(4, "Biologia"),
    Subject(5, "Programacion")
]

academic_hours = [
    Academic_Hour(1, "Lunes", "7:00", "7:40"),
    Academic_Hour(2, "Lunes", "7:40", "8:20"),
    Academic_Hour(3, "Lunes", "8:20", "9:00"),
    Academic_Hour(4, "Lunes", "9:00", "9:40"),
    Academic_Hour(5, "Lunes", "9:40", "10:20"),
    Academic_Hour(6, "Martes", "7:00", "7:40"),
    Academic_Hour(7, "Martes", "7:40", "8:20"),
    Academic_Hour(8, "Martes", "8:20", "9:00"),
    Academic_Hour(9, "Martes", "9:00", "9:40"),
    Academic_Hour(10, "Martes", "9:40", "10:20"),
    Academic_Hour(11, "Miercoles", "7:00", "7:40"),
    Academic_Hour(12, "Miercoles", "7:40", "8:20"),
    Academic_Hour(13, "Miercoles", "8:20", "9:00"),
    Academic_Hour(14, "Miercoles", "9:00", "9:40"),
    Academic_Hour(15, "Miercoles", "9:40", "10:20"),
    Academic_Hour(16, "Jueves", "7:00", "7:40"),
    Academic_Hour(17, "Jueves", "7:40", "8:20"),
    Academic_Hour(18, "Jueves", "8:20", "9:00"),
    Academic_Hour(19, "Jueves", "9:00", "9:40"),
    Academic_Hour(20, "Jueves", "9:40", "10:20"),
    Academic_Hour(21, "Viernes", "7:00", "7:40"),
    Academic_Hour(22, "Viernes", "7:40", "8:20"),
    Academic_Hour(23, "Viernes", "8:20", "9:00"),
    Academic_Hour(24, "Viernes", "9:00", "9:40"),
    Academic_Hour(25, "Viernes", "9:40", "10:20")
]

rooms = [
    Room(1, "Aula 1"),
    Room(2, "Aula 2"),
    Room(3, "Aula 3"),
    Room(4, "Aula 4"),
    Room(5, "Aula 5")
]

groups = [
    Group(1, "1ro A", [subjects[0], subjects[1]]),
    Group(2, "1ro B", [subjects[0], subjects[1]]),
    Group(3, "1ro C", [subjects[0], subjects[1]]),
    Group(4, "2do A", [subjects[1], subjects[2]]),
    Group(5, "2do B", [subjects[1], subjects[2]]),
    Group(6, "2do C", [subjects[1], subjects[2]]),
    Group(7, "3ro A", [subjects[2], subjects[3]]),
    Group(8, "3ro B", [subjects[2], subjects[3]]),
    Group(9, "3ro C", [subjects[2], subjects[3]])
]

def create_timetable(teachers, academic_hours, rooms, groups):
    timetable = []

    for group in groups:
        for subject in group.subjects:
            teacher = random.choice(teachers)
            academic_hour = random.choice(academic_hours)
            room = random.choice(rooms)

            timetable.append([group.id, subject.id, teacher.id, academic_hour.id, room.id])
    
    return timetable

def create_population(size):
    population = []

    for i in range(size):
        population.append(create_timetable(teachers, academic_hours, rooms, groups))
    
    return population

def groups_subjects(individual):
    score = 0
    groups_ocupation = {}

    for item in individual:
        g, s, t, a, r = item
        key = (g, a)

        if key in groups_ocupation:
            score += 5
        else:
            groups_ocupation[key] = s

    return score

def teachers_subjects(individual):
    score = 0
    teachers_ocupation = {}

    for item in individual:
        g, s, t, a, r = item
        key = (t, a)

        if key in teachers_ocupation:
            score += 5
        else:
            teachers_ocupation[key] = s

    return score

def rooms_groups(individual):
    score = 0
    rooms_ocupation = {}

    for item in individual:
        g, s, t, a, r = item
        key = (r, a)

        if key in rooms_ocupation:
            score += 5
        else:
            rooms_ocupation[key] = g

    return score

def fitness(population):
    results = []
    score = 0

    for individual in population:
        score = groups_subjects(individual) + teachers_subjects(individual) + rooms_groups(individual)
        results.append(score)
    
    return results

def main():
    population = create_population(100)
    scores = fitness(population)
    fitness_population = list(zip(scores, population))

#def print_population(population):
#    for i, (score, individual) in enumerate(population):
#        print(f"\n=== Horario #{i+1} | Fitness Score: {score} ===")
#        if i < 3: 
#            for item in individual:
#                g, s, t, a, r = item
#                print(f"  Sec: {g} | Mat: {s} | Prof: {t} | Bloque: {a} | Aula: {r}")
#        else:
#            print("  [... Otros horarios ocultos ...]")
#            break

if __name__ == "__main__":
    main()

