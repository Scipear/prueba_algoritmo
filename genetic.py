import numpy as np
import random
import copy
from classes import Teacher, Subject, Academic_Hour, Room, Group, Event

teachers = [
    Teacher(1, "Maria Lopez"),
    Teacher(2, "Juan Lopez"),
    Teacher(3, "Jose Lopez"),
    Teacher(4, "Roberta Lopez"),
    Teacher(5, "Luisa Lopez"),
    Teacher(6, "Carlos Perez"),
    Teacher(7, "Ana Rodriguez"),
    Teacher(8, "Pedro Gomez"),
    Teacher(9, "Laura Martinez"),
    Teacher(10, "Diego Hernandez"),
    Teacher(11, "Elena Diaz"),
    Teacher(12, "Miguel Garcia"),
    Teacher(13, "Sofia Torres"),
    Teacher(14, "Ricardo Sanchez"),
    Teacher(15, "Isabel Castro"),
    Teacher(16, "Fernando Romero"),
    Teacher(17, "Lucia Morales"),
    Teacher(18, "Gabriel Espinoza"),
    Teacher(19, "Valeria Ruiz"),
    Teacher(20, "Alejandro Leon"),
    Teacher(21, "Carmen Mendez"),
    Teacher(22, "Javier Soto"),
    Teacher(23, "Paola Delgado"),
    Teacher(24, "Andres Alvarado"),
    Teacher(25, "Beatriz Rojas"),
    Teacher(26, "Roberto Vivas"),
    Teacher(27, "Daniela Ortiz"),
    Teacher(28, "Marcos Silva"),
    Teacher(29, "Gloria Medina"),
    Teacher(30, "Samuel Herrera"),
    Teacher(31, "Patricia Aguilar")
]

subjects = [
    Subject(1, "Matematica", 4, [teachers[0], teachers[1], teachers[2], teachers[3]]),
    Subject(2, "Educacion Fisica", 2, [teachers[4]]),
    Subject(3, "Geografia, Historia y Soberania Nacional 1ro y 2do", 4, [teachers[5]]),
    Subject(4, "Biologia Ambiente y Tecnologia 1ro y 2do", 4, [teachers[6]]),
    Subject(5, "Idiomas 1ro y 2do", 3, [teachers[7]]),
    Subject(6, "Proyecto de Economia Socioproductiva y Tecnologia", 8, [teachers[8], teachers[9], teachers[10], teachers[11], teachers[12], teachers[13], teachers[14], teachers[15], teachers[16], teachers[17], teachers[18], teachers[19], teachers[20]]),
    Subject(7, "Maquinas, Distribucion y Control 1ro a 3ro", 8, [teachers[8], teachers[9]]),
    Subject(8, "Telecomunicacion y Control 1ro a 3ro", 8, [teachers[10], teachers[11]]),
    Subject(9, "Mantenimiento Maquinas 1ro a 3ro", 8, [teachers[12], teachers[13]]),
    Subject(10, "Sistema de Refrigeracion 1ro a 3ro", 8, [teachers[14], teachers[15]]),
    Subject(11, "Orientacion y Vinculacion Sociolaboral 1ro y 2do", 4, [teachers[24], teachers[8], teachers[9], teachers[10], teachers[11], teachers[12], teachers[13], teachers[14]]),
    Subject(12, "Lengua y Literatura 1ro y 2do", 3, [teachers[21]]),
    Subject(13, "Lengua y Literatura 3ro a 5to", 4, [teachers[22], teachers[23]]),
    Subject(14, "Idiomas 3ro a 5to", 4, [teachers[24], teachers[25]]),
    Subject(15, "Biologia Ambiente y Tecnologia 3ro a 5to", 8, [teachers[26], teachers[27], teachers[28], teachers[29]]),
    Subject(16, "Geografia, Historia y Soberania Nacional 3ro a 5to", 2, [teachers[30]]),
    Subject(17, "Maquinas, Distribucion y Control 4to y 5to", 10, [teachers[16]]),
    Subject(18, "Telecomunicacion y Control 4to y 5to", 10, [teachers[17], teachers[18]]),
    Subject(19, "Mantenimiento Maquinas 4to y 5to", 10, [teachers[19]]),
    Subject(20, "Sistema de Refrigeracion 4to y 5to", 10, [teachers[20]]),
    Subject(21, "Orientacion y Vinculacion Sociolaboral 3ro a 5to", 2, [teachers[10], teachers[20], teachers[19]]),
]

academic_hours = [
    Academic_Hour(1, "Lunes", "7:00", "7:40"),
    Academic_Hour(2, "Lunes", "7:40", "8:20"),
    Academic_Hour(3, "Lunes", "8:30", "9:10"),
    Academic_Hour(4, "Lunes", "9:10", "9:50"),
    Academic_Hour(5, "Lunes", "9:50", "10:30"),
    Academic_Hour(6, "Lunes", "10:30", "11:10"),
    Academic_Hour(7, "Lunes", "11:10", "11:50"),
    Academic_Hour(8, "Lunes", "12:10", "12:50"),
    Academic_Hour(9, "Lunes", "12:50", "1:30"),
    Academic_Hour(10, "Lunes", "1:30", "2:10"),
    Academic_Hour(11, "Martes", "7:00", "7:40"),
    Academic_Hour(12, "Martes", "7:40", "8:20"),
    Academic_Hour(13, "Martes", "8:30", "9:10"),
    Academic_Hour(14, "Martes", "9:10", "9:50"),
    Academic_Hour(15, "Martes", "9:50", "10:30"),
    Academic_Hour(16, "Martes", "10:30", "11:10"),
    Academic_Hour(17, "Martes", "11:10", "11:50"),
    Academic_Hour(18, "Martes", "12:10", "12:50"),
    Academic_Hour(19, "Martes", "12:50", "1:30"),
    Academic_Hour(20, "Martes", "1:30", "2:10"),
    Academic_Hour(21, "Miercoles", "7:00", "7:40"),
    Academic_Hour(22, "Miercoles", "7:40", "8:20"),
    Academic_Hour(23, "Miercoles", "8:30", "9:10"),
    Academic_Hour(24, "Miercoles", "9:10", "9:50"),
    Academic_Hour(25, "Miercoles", "9:50", "10:30"),
    Academic_Hour(26, "Miercoles", "10:30", "11:10"),
    Academic_Hour(27, "Miercoles", "11:10", "11:50"),
    Academic_Hour(28, "Miercoles", "12:10", "12:50"),
    Academic_Hour(29, "Miercoles", "12:50", "1:30"),
    Academic_Hour(30, "Miercoles", "1:30", "2:10"),
    Academic_Hour(31, "Jueves", "7:00", "7:40"),
    Academic_Hour(32, "Jueves", "7:40", "8:20"),
    Academic_Hour(33, "Jueves", "8:30", "9:10"),
    Academic_Hour(34, "Jueves", "9:10", "9:50"),
    Academic_Hour(35, "Jueves", "9:50", "10:30"),
    Academic_Hour(36, "Jueves", "10:30", "11:10"),
    Academic_Hour(37, "Jueves", "11:10", "11:50"),
    Academic_Hour(38, "Jueves", "12:10", "12:50"),
    Academic_Hour(39, "Jueves", "12:50", "1:30"),
    Academic_Hour(40, "Jueves", "1:30", "2:10"),
    Academic_Hour(41, "Viernes", "7:00", "7:40"),
    Academic_Hour(42, "Viernes", "7:40", "8:20"),
    Academic_Hour(43, "Viernes", "8:30", "9:10"),
    Academic_Hour(44, "Viernes", "9:10", "9:50"),
    Academic_Hour(45, "Viernes", "9:50", "10:30"),
    Academic_Hour(46, "Viernes", "10:30", "11:10"),
    Academic_Hour(47, "Viernes", "11:10", "11:50"),
    Academic_Hour(48, "Viernes", "12:10", "12:50"),
    Academic_Hour(49, "Viernes", "12:50", "1:30"),
    Academic_Hour(50, "Viernes", "1:30", "2:10")
    
]

rooms = [
    Room(1, "Aula 1"),
    Room(2, "Aula 2"),
    Room(3, "Aula 3"),
    Room(4, "Aula 4"),
    Room(5, "Aula 5"),
    Room(6, "Aula 6"),
    Room(7, "Aula 7"),
    Room(8, "Aula 8"),
    Room(9, "Aula 9"),
    Room(10, "Aula 10"),
    Room(11, "Aula 11"),
    Room(12, "Aula 12"),
    Room(13, "Aula 13"),
    Room(14, "Aula 14"),
    Room(15, "Aula 15"),
    Room(16, "Aula 16"),
    Room(17, "Aula 17"),
    Room(18, "Aula 18"),
    Room(19, "Aula 19"),
    Room(20, "Aula 20"),
    Room(21, "Aula 21"),
    Room(22, "Aula 22"),
    Room(23, "Aula 23"),
    Room(24, "Aula 24"),
    Room(25, "Aula 25")
]

groups = [
    Group(1, "1ro Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[6], subjects[10]]),
    Group(2, "1ro Electronica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7], subjects[10]]),
    Group(3, "1ro Telematica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[10]]),
    Group(4, "1ro Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[8], subjects[10]]),
    Group(5, "1ro Mecanica Termica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[9], subjects[10]]),
    Group(6, "2do Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[6], subjects[10]]),
    Group(7, "2do Electronica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7], subjects[10]]),
    Group(8, "2do Electronica B", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7], subjects[10]]),
    Group(9, "2do Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[8], subjects[10]]),
    Group(10, "2do Mecanica Termina A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[9], subjects[10]]),
    Group(11, "3ro Electricidad A", [subjects[12], subjects[13], subjects[0], subjects[1], subjects[14], subjects[15], subjects[5], subjects[6], subjects[20]]),
    Group(12, "3ro Electronica A", [subjects[12], subjects[13], subjects[0], subjects[1], subjects[14], subjects[15], subjects[5], subjects[7], subjects[20]]),
    Group(13, "3ro Electronica B", [subjects[12], subjects[13], subjects[0], subjects[1], subjects[14], subjects[15], subjects[5], subjects[7], subjects[20]]),
    Group(14, "3ro Metalmecanica A", [subjects[12], subjects[13], subjects[0], subjects[1], subjects[14], subjects[15], subjects[5], subjects[8], subjects[20]]),
    Group(15, "3ro Mecanica Termina A", [subjects[12], subjects[13], subjects[0], subjects[1], subjects[14], subjects[15], subjects[5], subjects[9], subjects[20]]),
    Group(16, "4to Electricidad A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[16], subjects[20]]),
    Group(17, "4to Electronica A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[17], subjects[20]]),
    Group(18, "4to Electronica B", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[17], subjects[20]]),
    Group(19, "4to Metalmecanica A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[18], subjects[20]]),
    Group(20, "4to Mecanica Termina A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[19], subjects[20]]),
    Group(21, "5to Electricidad A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[16], subjects[20]]),
    Group(22, "5to Electronica A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[17], subjects[20]]),
    Group(23, "5to Electronica B", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[17], subjects[20]]),
    Group(24, "5to Metalmecanica A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[18], subjects[20]]),
    Group(25, "5to Mecanica Termina A", [subjects[12], subjects[13], subjects[0], subjects[14], subjects[15], subjects[5], subjects[19], subjects[20]]),
]

def create_timetable(events: list[Event]):
    timetable = []

    for event in events:
        day = random.randint(0, 4)
        day_start = (day * 10) + 1
        event.start_hour = random.randint(day_start, (day_start + 10) - event.duration)
        event.room = random.choice(rooms).id
        timetable.append(event)
    
    return timetable

    # for group in groups:
    #     sorted_subjects = sorted(group.subjects, key=lambda s: s.hours, reverse=True)
    #     for subject in sorted_subjects:
    #         duration = subject.hours - 1
    #         teacher = random.choice(subject.teachers)
    #         timetable.append(create_class(group.id, subject.id, teacher.id, duration))
    
    # return timetable

def create_events():
    event_list = []
    id = 1

    for group in groups:
        sorted_subjects = sorted(group.subjects, key=lambda s: s.hours, reverse=True)

        for subject in sorted_subjects:
            left_hours = subject.hours
            teacher = random.choice(subject.teachers)

            while left_hours > 0:
                if left_hours >= 8:
                    duration = random.randint(6, left_hours)
                
                elif left_hours > 2:
                    duration = random.randint(2, left_hours)

                else:
                    duration = left_hours

                event_list.append(Event(id, teacher, subject, group, duration))
                id += 1
                left_hours -= duration
    
    return event_list

# def create_class(group_id, subject_id, teacher_id, duration):
    subject_classes = []
    special_subjects = [7, 8, 9, 10, 17, 18, 19, 20]

    while duration >= 0:
        start_hour = random.choice(academic_hours)
        day_end_id = ((start_hour.id - 1) // 10 + 1) * 10
        room = random.choice(rooms)

        if duration >= 3:
            point = random.randint(1, duration - 1)

            if subject_id in special_subjects and duration >= 6:
                if duration >= 7:
                    start_hour = academic_hours[((start_hour.id - 1) // 10) * 10 ]
                    point = duration
                else:
                    point = random.randint(6, duration - 1)

            if start_hour.id + point - 1 > day_end_id:
                point = day_end_id - start_hour.id + 1
            
            if start_hour.id + point <= len(academic_hours):
                end_hour = academic_hours[(start_hour.id + point) - 1]
                duration = (duration - point) - 1
            else:
                end_hour = academic_hours[len(academic_hours) - 1]
                duration -= ((end_hour.id - start_hour.id) + 1)
            
            subject_classes.append([group_id, subject_id, teacher_id, start_hour.id, end_hour.id, room.id])
            
            while True:
                start_hour = random.choice(academic_hours)

                if start_hour != end_hour:
                    break
            
            room = random.choice(rooms)
        
        if start_hour.id + duration < len(academic_hours):
            end_hour = academic_hours[(start_hour.id + duration) - 1]
            duration = -1

        else:
            end_hour = academic_hours[len(academic_hours) - 1]
            duration -= ((end_hour.id - start_hour.id) + 1)
        
        subject_classes.append([group_id, subject_id, teacher_id, start_hour.id, end_hour.id, room.id])
    
    return subject_classes

def create_population(size: int, events: list[Event]):
    population = []

    for i in range(size):
        original_timetable = create_timetable(events)
        timetable_copy = copy.deepcopy(original_timetable)
        population.append(timetable_copy)
    
    return population

def fitness(population: list[list[Event]]):
    results = []
    score = 0
    i = 0

    for individual in population:
        i += 1
        score = groups_subjects(individual) + teachers_subjects(individual) + rooms_groups(individual)
        results.append(score)

    return results
        

def groups_subjects(individual: list[Event]):
    score = 0
    groups_occupation = {}

    for event in individual:
        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.group, block)

            if key in groups_occupation:
                score += 5
            else:
                groups_occupation[key] = event
    
    return score

    # for subject in individual:
    #     for block in subject:
    #         g, s, t, s_h, e_h, r = block

    #         for hour_id in range(s_h, e_h + 1):
    #             key = (g, hour_id)

    #             if key in groups_occupation:
    #                 score += 5
    #             else:
    #                 groups_occupation[key] = s

    # return score

def teachers_subjects(individual: list[Event]):
    score = 0
    teachers_occupation = {}

    for event in individual:
        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.teacher, block)

            if key in teachers_occupation:
                score += 5
            else:
                teachers_occupation[key] = event
    
    return score

    # for subject in individual:
    #     for block in subject:
    #         g, s, t, s_h, e_h, r = block

    #         for hour_id in range(s_h, e_h + 1):
    #             key = (t, hour_id)

    #             if key in teachers_occupation:
    #                 score += 5
    #             else:
    #                 teachers_occupation[key] = s

def rooms_groups(individual: list[Event]):
    score = 0
    rooms_occupation = {}

    for event in individual:
        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.room, block)

            if key in rooms_occupation:
                score += 5
            else:
                rooms_occupation[key] = event
    
    return score

    # for subject in individual:
    #     for block in subject:
    #         g, s, t, s_h, e_h, r = block

    #         for hour_id in range(s_h, e_h + 1):

    #             key = (r, hour_id)

    #             if key in rooms_occupation:
    #                 score += 5
    #             else:
    #                 rooms_occupation[key] = g

    # return score

def selection(population, size):

    population.sort(key=lambda x: x[0])
    selected_population = population[:size]

    return selected_population

def crossover(selected_population: list[list[Event]], population_size: int):
    new_population = []

    new_population.append(copy.deepcopy(selected_population[0][1]))
    new_population.append(copy.deepcopy(selected_population[1][1]))

    while len(new_population) < population_size:
        parents = random.sample(selected_population, 2)
        p1, p2 = parents[0][1], parents[1][1]
        
        point = random.randint(1, len(p1) - 1)
        child = copy.deepcopy(p1[:point] + p2[point:])
        
        child = mutation(child)
        new_population.append(child)
        
    return new_population

def mutation(individual: list[Event]):
    for event in individual:
        if random.random() < 0.05:
            if random.choice([True, False]):
                day = random.randint(0, 4)
                day_start = (day * 10) + 1
                event.start_hour = random.randint(day_start, (day_start + 10) - event.duration)
            else:
                event.room = random.choice(rooms).id
    
    return individual

    # for i in range(len(individual)):
    #     if random.random() <= 0.15:
    #         #teacher = random.choice(subjects[individual[i][0][1] - 1].teachers)
    #         j = random.randint(0, len(individual[i]) - 1)
    #         s_h = individual[i][j][3]
    #         e_h = individual[i][j][4]
    #         duration = e_h - s_h
            
    #         offset = random.choice([-1, 1])
    #         new_s = s_h + offset
    #         new_e = new_s + duration
            
    #         start_day = ((s_h - 1) // 10) * 10 + 1
    #         end_day = start_day + 9
            
    #         if start_day <= new_s and new_e <= end_day:
    #             individual[i][j][3] = new_s
    #             individual[i][j][4] = new_e
    #         # for j in range(len(individual[i])):
    #         #     g, s, t, s_h, e_h, r = individual[i][j]
    #         #     duration += (e_h - s_h) + 1
            
    #         # individual[i] = create_class(individual[i][0][0], individual[i][0][1], teacher.id, duration)
    
    # return individual

def main():
    events = create_events()
    i = 0
    population = create_population(100, events)

    while i < 1000:
        scores = fitness(population)
        fitness_population = list(zip(scores, population))
        if i == 0:
            print("Poblacion sin seleccionar")
            print_population(fitness_population)
        elif i % 10 == 0:
            fitness_population.sort(key=lambda x: x[0])
            print(f"Generacion {i} - Mejor Fitness: {fitness_population[0][0]}")

        selected_population = selection(fitness_population, 10)
        if i == 0:
            print("Poblacion seleccionada")
            print_population(selected_population)
        
        population = crossover(selected_population, 100)
        i += 1
    
    # scores = fitness(population)
    # fitness_population = list(zip(scores, population))
    # fitness_population.sort(key=lambda x: x[0])
    # print("generacion 100 ordenada")
    # print_population(fitness_population)

def print_population(population: list[list[Event]]):
    for i, (score, individual) in enumerate(population):
        print(f"\n=== Horario #{i+1} | Fitness Score: {score} ===")
        if i < 1:
            for event in individual:
                print(event)
        #     for subject in individual:
        #         for block in subject:
        #             g, s, t, s_h, e_h, r = block
        #             print(f"  Sec: {g} | Mat: {s} | Prof: {t} | Inicio: {s_h} | Fin: {e_h} | Aula: {r}")
                    
        # else:
        #     print("  [... Otros horarios ocultos ...]")
        #     break

if __name__ == "__main__":
    main()

