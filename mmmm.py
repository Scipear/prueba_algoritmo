def create_timetable():
    timetable = []

    for group in groups:
        for subject in group.subjects:
            hours = subject.hours
            teacher = random.choice(subject.teachers)
            timetable.append(create_class(group.id, subject.id, teacher.id, hours))
    
    return timetable

def create_class(group_id, subject_id, teacher_id, hours):
    subject_classes = []
    hours_left = hours

    while hours_left > 0:
        start_hour = random.choice(academic_hours)
        day_end_id = ((start_hour.id - 1) // 10 + 1) * 10

        if hours_left >= 4:
            block_hours = random.randint(2, min(3, hours_left - 1))
        else:
            block_hours = hours_left
            
        if start_hour.id + block_hours - 1 > day_end_id:
            block_hours = day_end_id - start_hour.id + 1
            
        end_hour_id = start_hour.id + block_hours - 1
            
        room = random.choice(rooms)
        subject_classes.append([group_id, subject_id, teacher_id, start_hour.id, end_hour_id, room.id])
        
        hours_left -= block_hours
    
    return subject_classes

def create_population(size):
    population = []

    for i in range(size):
        population.append(create_timetable())
    
    return population

def groups_subjects(individual):
    score = 0
    groups_occupation = {}

    for subject in individual:
        for block in subject:
            g, s, t, s_h, e_h, r = block

            for hour_id in range(s_h, e_h + 1):
                key = (g, hour_id)

                if key in groups_occupation:
                    score += 5
                else:
                    groups_occupation[key] = s

    return score

def teachers_subjects(individual):
    score = 0
    teachers_occupation = {}

    for subject in individual:
        for block in subject:
            g, s, t, s_h, e_h, r = block

            for hour_id in range(s_h, e_h + 1):
                key = (t, hour_id)

                if key in teachers_occupation:
                    score += 5
                else:
                    teachers_occupation[key] = s

    return score

def rooms_groups(individual):
    score = 0
    rooms_occupation = {}

    for subject in individual:
        for block in subject:
            g, s, t, s_h, e_h, r = block

            for hour_id in range(s_h, e_h + 1):

                key = (r, hour_id)

                if key in rooms_occupation:
                    score += 5
                else:
                    rooms_occupation[key] = g

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

def crossover(selected_population, population_size):
    new_population = []

    new_population.append(copy.deepcopy(selected_population[0][1]))
    new_population.append(copy.deepcopy(selected_population[1][1]))

    while len(new_population) < population_size:
        parents = random.sample(selected_population, 2)
        p1, p2 = parents[0][1], parents[1][1]
        
        point = random.randint(1, len(p1) - 1)
        child = copy.deepcopy(p1[:point]) + copy.deepcopy(p2[point:])
        
        child = mutation(child)
        new_population.append(child)
        
    return new_population

def mutation(individual):
    for i in range(len(individual)):
        if random.random() <= 0.15:
            hours = sum((block[4] - block[3] + 1) for block in individual[i])
            teacher = random.choice(subjects[individual[i][0][1] - 1].teachers)
            
            individual[i] = create_class(individual[i][0][0], individual[i][0][1], teacher.id, hours)
    
    return individual

def main():
    i = 0
    population = create_population(100)
    
    while i < 100:
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
    
    scores = fitness(population)
    fitness_population = list(zip(scores, population))
    fitness_population.sort(key=lambda x: x[0])
    print("generacion 100 ordenada")
    print_population(fitness_population)