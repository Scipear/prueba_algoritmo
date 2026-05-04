import numpy as np
import random
from classes import Teacher, Subject, Academic_Hour, Room, Group

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
    Subject(1, "Matematica"),
    Subject(2, "Educacion Fisica"),
    Subject(3, "Geografia, Historia y Soberania Nacional"),
    Subject(4, "Biologia Ambiente y Tecnologia"),
    Subject(5, "Idiomas"),
    Subject(6, "Proyecto de Economia Socioproductiva y Tecnologia"),
    Subject(7, "Maquinas, Distribucion y Control"),
    Subject(8, "Telecomunicacion y Control"),
    Subject(9, "Mantenimiento Maquinas"),
    Subject(10, "Sistema de Refrigeracion"),
    Subject(11, "Orientacion y Vinculacion Sociolaboral"),
    Subject(12, "Lengua y Literatura"),
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
    Group(1, "1ro Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[6]]),
    Group(2, "1ro Electronica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(3, "1ro Telematica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5]]),
    Group(4, "1ro Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[8]]),
    Group(5, "1ro Mecanica Termica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[9]]),
    Group(6, "2do Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[6]]),
    Group(7, "2do Electronica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(8, "2do Electronica B", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(9, "2do Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[8]]),
    Group(10, "2do Mecanica Termina A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[9]]),
    Group(11, "3ro Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[6]]),
    Group(12, "3ro Electronica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(13, "3ro Electronica B", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(14, "3ro Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[8]]),
    Group(15, "3ro Mecanica Termina A", [subjects[11], subjects[4], subjects[0], subjects[1], subjects[3], subjects[2], subjects[5], subjects[9]]),
    Group(16, "4to Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[6]]),
    Group(17, "4to Electronica A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(18, "4to Electronica B", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(19, "4to Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[8]]),
    Group(20, "4to Mecanica Termina A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[9]]),
    Group(21, "5to Electricidad A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[6]]),
    Group(22, "5to Electronica A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(23, "5to Electronica B", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[7]]),
    Group(24, "5to Metalmecanica A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[8]]),
    Group(25, "5to Mecanica Termina A", [subjects[11], subjects[4], subjects[0], subjects[3], subjects[2], subjects[5], subjects[9]]),
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

def selection(population, size):

    population.sort(key=lambda x: x[0])
    selected_population = population[:size]

    return selected_population

def crossover(population, selected_population):
    point = 0
    parents = []

    for i in range(len(population)):
        point = np.random.randint(1, len(population[i]) - 1)
        parents = random.sample(selected_population, 2)

        population[i][:point] = parents[0][1][:point]
        population[i][point:] = parents[1][1][point:]

        population[i] = mutation(population[i])
    
    return population

def mutation(individual):
    for i in range(len(individual)):
        if random.random() <= 0.1:
            academic_hour = random.choice(academic_hours)

            individual[i] = [individual[i][0], individual[i][1], individual[i][2], academic_hour.id, individual[i][4]]
    
    return individual



def main():
    i = 0
    population = create_population(50)

    while i < 100:
        scores = fitness(population)
        fitness_population = list(zip(scores, population))

        if i == 0:
            print("Poblacion sin seleccionar")
            print_population(fitness_population)
        selected_population = selection(fitness_population, 15)
        
        if i == 0:
            print("Poblacion seleccionada")
            print_population(selected_population)
        population = crossover(population, selected_population)
        
        i += 1

    scores = fitness(population)
    fitness_population = list(zip(scores, population))
    fitness_population.sort(key=lambda x: x[0])
    print("generacion 100 ordenada")
    print_population(fitness_population)

def print_population(population):
    for i, (score, individual) in enumerate(population):
        print(f"\n=== Horario #{i+1} | Fitness Score: {score} ===")
        if i < 1: 
            for item in individual:
                g, s, t, a, r = item
                print(f"  Sec: {g} | Mat: {s} | Prof: {t} | Bloque: {a} | Aula: {r}")
        else:
            print("  [... Otros horarios ocultos ...]")
            break

if __name__ == "__main__":
    main()

