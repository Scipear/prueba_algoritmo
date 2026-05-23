import numpy as np
import random
import copy
from classes import Teacher, Subject, Academic_Hour, Room, Group, Availability, Event

availabilities = [
    Availability(1, 1, 10),
    Availability(2, 11, 20),
    Availability(3, 21, 30),
    Availability(4, 31, 40),
    Availability(5, 41, 50),
    Availability(6, 1, 7),
    Availability(7, 11, 17),
    Availability(8, 21, 27),
    Availability(9, 31, 37),
    Availability(10, 41, 47),
    Availability(11, 35, 40),
    Availability(12, 1, 6),
    Availability(13, 11, 18),
    Availability(14, 21, 26),
    Availability(15, 31, 36),
    Availability(16, 41, 46),
    Availability(17, 11, 16),

]

teachers = [
    Teacher(1, "Yhisel Bethermy", [availabilities[2], availabilities[3], availabilities[4]]), 
    Teacher(2, "Yelkis Carrasquero", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(3, "Lisbeth Contreras", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(4, "Elias Gonzales", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(5, "Greudisep Gonzales", [availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(6, "Emma Guzman", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(7, "Nancy Hernandez", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(8, "Carmen Itanare", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(9, "Maria Marcano", [availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(10, "Pedro Martinez", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(11, "Margaret Mendoza", [availabilities[0], availabilities[1], availabilities[3], availabilities[7], availabilities[9]]),
    Teacher(12, "Keylimar Pacheco", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(13, "Claritza Rodriguez", [availabilities[0], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(14, "Yudilernis Romero", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(15, "Yeesika Rondon", [availabilities[11], availabilities[12], availabilities[13], availabilities[14], availabilities[15]]),
    Teacher(16, "Yoandris Vallenilla", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(17, "Julio Aguilar", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(18, "Brenda Alcala", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(19, "Rocio Centeno", [availabilities[0], availabilities[1], availabilities[14], availabilities[15], availabilities[16]]),
    Teacher(20, "Yosmarys Gil", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(21, "Jose Guevara", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(22, "Yesenia Mundarain", [availabilities[0], availabilities[1], availabilities[3], availabilities[4], availabilities[4]]),
    Teacher(23, "Margred Palacios", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(24, "Joanna Pinto", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(25, "Silvia Plaza", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(26, "Arlene Rivera", [availabilities[2], availabilities[3]]),
    Teacher(27, "Yoxiana Rodriguez", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(28, "Danyer Teran", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(29, "Magaly Valderrama", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(30, "Anne Albornoz", [availabilities[11], availabilities[13], availabilities[14], availabilities[15], availabilities[16]]),
    Teacher(31, "Juan Toro", [availabilities[0], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(32, "Niurka Pinto", [availabilities[0], availabilities[1], availabilities[2]])
]

subjects = [
    Subject(1, "Matematica", 4, [teachers[14], teachers[15], teachers[29], teachers[30]]),
    Subject(2, "Educacion Fisica", 2, [teachers[9]]),
    Subject(3, "Geografia, Historia y Soberania Nacional 1ro y 2do", 4, [teachers[4], teachers[8]]),
    Subject(4, "Biologia Ambiente y Tecnologia 1ro y 2do", 4, [teachers[12]]),
    Subject(5, "Idiomas 1ro y 2do", 3, [teachers[1]]),
    Subject(6, "Proyecto de Economia Socioproductiva y Tecnologia", 8, [teachers[14], teachers[16], teachers[17], teachers[18], teachers[19], teachers[20], teachers[21], teachers[22], teachers[23], teachers[24], teachers[26], teachers[27], teachers[28], teachers[31]]),
    Subject(7, "Maquinas, Distribucion y Control 1ro a 3ro", 8, [teachers[24], teachers[25]]),
    Subject(8, "Telecomunicacion y Control 1ro a 3ro", 8, [teachers[19], teachers[22], teachers[23]]),
    Subject(9, "Mantenimiento Maquinas 1ro a 3ro", 8, [teachers[14], teachers[20]]),
    Subject(10, "Sistema de Refrigeracion 1ro a 3ro", 8, [teachers[18], teachers[27]]),
    Subject(11, "Orientacion y Vinculacion Sociolaboral 1ro y 2do", 4, [teachers[18], teachers[20], teachers[22], teachers[23], teachers[24], teachers[25], teachers[27], teachers[0]]),
    Subject(12, "Lengua y Literatura 1ro y 2do", 3, [teachers[11]]),
    Subject(13, "Lengua y Literatura 3ro a 5to", 4, [teachers[2], teachers[3], teachers[11]]),
    Subject(14, "Idiomas 3ro a 5to", 4, [teachers[0], teachers[7]]),
    Subject(15, "Biologia Ambiente y Tecnologia 3ro a 5to", 8, [teachers[5], teachers[6], teachers[10], teachers[13]]),
    Subject(16, "Geografia, Historia y Soberania Nacional 3ro a 5to", 2, [teachers[8]]),
    Subject(17, "Maquinas, Distribucion y Control 4to y 5to", 10, [teachers[17]]),
    Subject(18, "Telecomunicacion y Control 4to y 5to", 10, [teachers[17], teachers[18], teachers[21], teachers[28], teachers[31]]),
    Subject(19, "Mantenimiento Maquinas 4to y 5to", 10, [teachers[16]]),
    Subject(20, "Sistema de Refrigeracion 4to y 5to", 10, [teachers[26]]),
    Subject(21, "Orientacion y Vinculacion Sociolaboral 3ro a 5to", 2, [teachers[16], teachers[18], teachers[19], teachers[5]]),
    Subject(22, "Programacion y Diseno de Software", 8, [teachers[23]])
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
    Room(25, "Aula 25"),
    Room(26, "Aula 26"),
    Room(27, "Aula 27"),
    Room(28, "Aula 28"),
    Room(29, "Aula 29"),
    Room(30, "Aula 30")
]

groups = [
    Group(1, "1ro Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[6], subjects[10]]),
    Group(2, "1ro Electronica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7], subjects[10]]),
    Group(3, "1ro Telematica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[10], subjects[21]]),
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

def random_start_hour(duration: int) -> int:
    day = random.randint(0, 4)
    day_start = (day * 10) + 1
    return random.randint(day_start, (day_start + 10) - duration)

def is_teacher_available(teacher: Teacher, start_hour: int, duration: int) -> bool:
    if teacher is None:
        return False
        
    event_hours = set(range(start_hour, start_hour + duration))
    
    for av in teacher.availabilities:
        av_hours = set(range(av.start_hour, av.end_hour + 1))
        if event_hours.issubset(av_hours):
            return True
            
    return False

def move_hour(start_hour: int, duration: int) -> int:
    day = (start_hour - 1) // 10
    start_hour_day = (day * 10) + 1
    end_hour_day = start_hour_day + 9

    if start_hour > start_hour_day:
        return start_hour - 1
    else:
        if day > 0:
            return start_hour_day - duration
        else:
            return (len(academic_hours) + 1) - duration

def create_timetable(events: list[Event]):
    timetable = []
    groups_block = {}
    teachers_block = {}

    for event in events:
        if event.group.id not in groups_block:
            groups_block[event.group.id] = set()

        if event.teacher.id not in teachers_block:
            teachers_block[event.teacher.id] = set()

        found_block = False
        start_hour = random_start_hour(event.duration)

        for _ in range(100):
            event_hours = range(start_hour, start_hour + event.duration)

            if (not groups_block[event.group.id].intersection(event_hours) and 
                not teachers_block[event.teacher.id].intersection(event_hours) and 
                is_teacher_available(event.teacher, start_hour, event.duration)):
                
                event.start_hour = start_hour
                if event.subject.id != 2:
                    event.room = random.choice(rooms)

                groups_block[event.group.id].update(event_hours)
                teachers_block[event.teacher.id].update(event_hours)
                found_block = True
                break

            start_hour = move_hour(start_hour, event.duration)
        
        if not found_block:
            start_hour = random_start_hour(event.duration)

            for _ in range(100):
                event_hours = range(start_hour, start_hour + event.duration)
                
                if not groups_block[event.group.id].intersection(event_hours) and is_teacher_available(event.teacher, start_hour, event.duration):
                    event.start_hour = start_hour
                    if event.subject.id != 2:
                        event.room = random.choice(rooms)
                    groups_block[event.group.id].update(event_hours)
                    teachers_block[event.teacher.id].update(event_hours) 
                    found_block = True
                    break

                start_hour = move_hour(start_hour, event.duration)

            if not found_block:
                possible_hours = []

                if event.teacher:
                    for av in event.teacher.availabilities:
                        for h in range(av.start_hour, (av.end_hour - event.duration) + 2):
                            possible_hours.append(h)

                if possible_hours:
                    event.start_hour = random.choice(possible_hours)
                else:
                    event.start_hour = random_start_hour(event.duration)

                if event.subject.id != 2:
                    event.room = random.choice(rooms)
                event_hours = range(event.start_hour, event.start_hour + event.duration)
                groups_block[event.group.id].update(event_hours)
                teachers_block[event.teacher.id].update(event_hours)

        timetable.append(event)
    
    return timetable

def create_events():
    event_list = []
    id = 1

    for group in groups:
        sorted_subjects = sorted(group.subjects, key=lambda s: s.hours, reverse=True)

        for subject in sorted_subjects:
            left_hours = subject.hours
            teacher = random.choice(subject.teachers)

            while left_hours > 0:
                if left_hours > 7 and left_hours < 10:
                    duration = random.choice([6, 8])
                
                elif left_hours > 2 and left_hours < 7:
                    if left_hours == 4:
                        duration = 2
                    else:
                        duration = random.randint(2, left_hours)

                else:
                    duration = left_hours

                event_list.append(Event(id, teacher, subject, group, duration))
                id += 1
                left_hours -= duration
    
    return event_list

def create_population(size: int, events: list[Event]):
    population = []

    for i in range(size):
        original_timetable = create_timetable(events)
        timetable_copy = copy.deepcopy(original_timetable)
        population.append(timetable_copy)
    
    return population

def fitness(population: list[list[Event]]):
    results = []
    
    for individual in population:
        # Extraemos el score y descartamos la lista de choques usando ', _'
        t_score, _ = teachers_subjects(individual)
        
        score = groups_subjects(individual) + t_score + rooms_groups(individual)
        results.append(score)

    return results
        

def groups_subjects(individual: list[Event]):
    score = 0
    groups_occupation = {}

    for event in individual:
        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.group.id, block)

            if key in groups_occupation:
                score += 0
            else:
                groups_occupation[key] = event
    
    return score

def teachers_subjects(individual: list[Event]):
    score = 0
    teachers_occupation = {}
    collisions = [] # Guardará el registro detallado de los choques

    for event in individual:
        # Ignorar eventos que no tienen hora asignada aún (preventivo)
        if event.start_hour is None:
            continue

        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.teacher.id, block)

            if key in teachers_occupation:
                score += 5
                
                # Evento con el que choca (el que ya estaba guardado en esa hora)
                existing_event = teachers_occupation[key]
                
                # Registramos el choque detallando ambos eventos involucrados
                collisions.append({
                    "teacher_id": event.teacher.name,
                    "block": block,
                    "event_1": {
                        "id": existing_event.id,
                        "subject": existing_event.subject.name,
                        "group": existing_event.group.name
                    },
                    "event_2": {
                        "id": event.id,
                        "subject": event.subject.name,
                        "group": event.group.name
                    }
                })
            else:
                teachers_occupation[key] = event
    
    return score, collisions

def rooms_groups(individual: list[Event]):
    score = 0
    rooms_occupation = {}

    for event in individual:
        for block in range(event.start_hour, event.start_hour + event.duration):
            if event.room != None:
                key = (event.room.id, block)

                if key in rooms_occupation:
                    score += 0
                else:
                    rooms_occupation[key] = event
    
    return score

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
        if random.random() < 0.02:
            if random.choice([True, False]):
                current_subject = event.subject
                available_teachers = []
                if current_subject:
                    for teacher in current_subject.teachers:
                        if is_teacher_available(teacher, event.start_hour, event.duration):
                            available_teachers.append(teacher)

                # DECISIÓN INTELIGENTE: Si hay profesores alternativos, tiramos una moneda (50/50).
                # Si el profesor es ÚNICO, lo obligamos a ir directamente a MUTAR HORA.
                mutar_profesor = False
                if available_teachers and random.choice([True, False]):
                    mutar_profesor = True

                if mutar_profesor:
                    # --- MUTAR PROFESOR ---
                    new_teacher = random.choice(available_teachers)
                    i_subject = event.subject.id
                    i_group = event.group.id

                    for e in individual:
                        if e.group.id > i_group:
                            break
                        if e.subject.id == i_subject and e.group.id == i_group:
                            e.teacher = new_teacher
                        
                else:
                    # --- MUTAR HORA ---
                    taken_hours = set()

                    # CORRECCIÓN CRÍTICA: Bloqueamos las horas donde el grupo YA tiene clases
                    # Y TAMBIÉN las horas donde este profesor YA está dictando otra clase en el instituto
                    for e in individual:
                        if e.start_hour is not None:
                            # Si es del mismo grupo O es el mismo profesor, esa hora NO está disponible
                            if e.group.id == event.group.id or e.teacher.id == event.teacher.id:
                                taken_hours.update(range(e.start_hour, e.start_hour + e.duration))
                    
                    available_space = False

                    # Intentamos buscar una hora aleatoria que no choque con nadie (Grupo o Profesor)
                    # Subimos los intentos a 100 para dar más margen de búsqueda limpia
                    for _ in range(100):
                        new_hour = random_start_hour(event.duration)
                        hours_block = range(new_hour, new_hour + event.duration)

                        # Si no colisiona con las horas ocupadas globales Y el profesor está disponible en su contrato
                        if not taken_hours.intersection(hours_block) and is_teacher_available(event.teacher, new_hour, event.duration):
                            event.start_hour = new_hour
                            available_space = True
                            break
                    
                    # Fallback de emergencia si el horario está muy apretado:
                    # Lo movemos a cualquier hora donde el profesor esté disponible según contrato 
                    # (aunque arriesguemos un choque de grupo que el fitness resolverá)
                    if not available_space:
                        valid_hours_for_prof = []
                        
                        if event.teacher:
                            for av in event.teacher.availabilities:
                                for h in range(av.start_hour, (av.end_hour - event.duration) + 2):
                                    valid_hours_for_prof.append(h)
                                    
                        if valid_hours_for_prof:
                            event.start_hour = random.choice(valid_hours_for_prof)
        else:
            if random.random() < 0.01 and event.subject.id != 2:
                event.room = random.choice(rooms)
    
    return individual

def main():
    events = create_events()
    i = 0
    population = create_population(50, events)

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
        
        population = crossover(selected_population, 50)
        i += 1
    
    scores = fitness(population)
    fitness_population = list(zip(scores, population))
    fitness_population.sort(key=lambda x: x[0])
    print("generacion 100 ordenada")
    print_population(fitness_population)
    best_individual = fitness_population[0][1] 
    _, final_collisions = teachers_subjects(best_individual)
    print_collisions_report(final_collisions)

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

def print_collisions_report(collisions: list):
    if not collisions:
        print("\n" + "="*50)
        print(" 🎉 ¡EXCELENTE! No se encontraron choques de profesores. 🎉")
        print("="*50 + "\n")
        return

    days_names = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    print("\n" + "!"*60)
    print(f"       REPORTE DETALLADO DE CHOQUES ({len(collisions)} detectados)")
    print("!"*60)

    # Agrupamos o iteramos para mostrarlo visualmente limpio
    for i, c in enumerate(collisions, 1):
        # Calcular el día (0 a 4) y la hora dentro de ese día (1 a 10)
        day_index = (c["block"] - 1) // 10
        hour_in_day = ((c["block"] - 1) % 10) + 1
        
        day_name = days_names[day_index] if day_index < len(days_names) else f"Día {day_index}"

        print(f"\n💥 CHOQUE #{i} | Profesor ID: {c['teacher_id']} | {day_name} - Hora Bloque: {hour_in_day} (Global: {c['block']})")
        print(f"  └─ Clase A: Evento ID {c['event_1']['id']} | Materia ID: {c['event_1']['subject']} | Grupo ID: {c['event_1']['group']}")
        print(f"  └─ Clase B: Evento ID {c['event_2']['id']} | Materia ID: {c['event_2']['subject']} | Grupo ID: {c['event_2']['group']}")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()