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
    Teacher(15, "Yeesika Rondon", [availabilities[11], availabilities[1], availabilities[13], availabilities[14], availabilities[15]]),
    Teacher(16, "Yoandris Vallenilla", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(17, "Julio Aguilar", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(18, "Brenda Alcala", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(19, "Rocio Centeno", [availabilities[0], availabilities[1], availabilities[14], availabilities[15], availabilities[16]]),
    Teacher(20, "Yosmarys Gil", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(21, "Jose Guevara", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(22, "Yesenia Mundarain", [availabilities[0], availabilities[1], availabilities[3], availabilities[4], availabilities[4]]),
    Teacher(23, "Margred Palacios", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(24, "Joanna Pinto", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(25, "Silvia Plaza", [availabilities[0], availabilities[1], availabilities[2], availabilities[3]]),
    Teacher(26, "Arlene Rivera", [availabilities[2], availabilities[3]]),
    Teacher(27, "Yoxiana Rodriguez", [availabilities[0], availabilities[1], availabilities[2], availabilities[4]]),
    Teacher(28, "Danyer Teran", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(29, "Magaly Valderrama", [availabilities[0], availabilities[1], availabilities[3], availabilities[4]]),
    Teacher(30, "Anne Albornoz", [availabilities[11], availabilities[13], availabilities[14], availabilities[15], availabilities[16]]),
    Teacher(31, "Juan Toro", [availabilities[0], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(32, "Niurka Pinto", [availabilities[0], availabilities[1], availabilities[2]]),
    Teacher(33, "Leosvel Castillo", [availabilities[1], availabilities[2], availabilities[3], availabilities[4]]),
    Teacher(34, "Karina Garcia", [availabilities[0], availabilities[1], availabilities[2], availabilities[3], availabilities[4]])

]

subjects = [
    Subject(1, "Lengua y Literatura 1ro", 3, [teachers[11]]),
    Subject(2, "Lengua y Literatura 2do", 3, [teachers[11]]),
    Subject(3, "Lengua y Literatura 3ro", 4, [teachers[3], teachers[11]]),
    Subject(4, "Lengua y Literatura 4to", 4, [teachers[3]]),
    Subject(5, "Lengua y Literatura 5to", 4, [teachers[2]]),
    Subject(6, "Ingles 1ro", 3, [teachers[1]]),
    Subject(7, "Ingles 2do", 3, [teachers[1]]),
    Subject(8, "Ingles 3ro", 4, [teachers[0]]),
    Subject(9, "Ingles 4to", 4, [teachers[0], teachers[7]]),
    Subject(10, "Ingles 5to", 4, [teachers[7]]),
    Subject(11, "Matematica 1ro", 4, [teachers[15]]),
    Subject(12, "Matematica 2do", 4, [teachers[14], teachers[15]]),
    Subject(13, "Matematica 3ro", 4, [teachers[14], teachers[30]]),
    Subject(14, "Matematica 4to", 4, [teachers[29], teachers[30]]),
    Subject(15, "Matematica 5to", 4, [teachers[29]]),
    Subject(16, "Educacion Fisica 1ro", 2, [teachers[9]]),
    Subject(17, "Educacion Fisica 2do", 2, [teachers[9]]),
    Subject(18, "Educacion Fisica 3ro", 2, [teachers[9]]),
    Subject(19, "Biologia, Ambiente y Tecnologia 1ro", 4, [teachers[12]]),
    Subject(20, "Biologia, Ambiente y Tecnologia 2ro", 4, [teachers[12], teachers[5]]),
    Subject(21, "Biologia, Ambiente y Tecnologia 3ro", 4, [teachers[13]]),
    Subject(22, "Biologia, Ambiente y Tecnologia (B) 3ro", 4, [teachers[6]]),
    Subject(23, "Biologia, Ambiente y Tecnologia (B) 4to", 2, [teachers[6]]),
    Subject(24, "Biologia, Ambiente y Tecnologia (F) 4to", 3, [teachers[10]]),
    Subject(25, "Biologia, Ambiente y Tecnologia (Q) 4to", 3, [teachers[13]]),
    Subject(26, "Biologia, Ambiente y Tecnologia (B) 5to", 4, [teachers[5]]),
    Subject(27, "Biologia, Ambiente y Tecnologia (F) 5to", 4, [teachers[10]]),
    Subject(28, "Geografia, Historia y Soberania Nacional 1ro", 4, [teachers[4]]),
    Subject(29, "Geografia, Historia y Soberania Nacional 2do", 4, [teachers[4], teachers[8]]),
    Subject(30, "Geografia, Historia y Soberania Nacional 3ro", 2, [teachers[8]]),
    Subject(31, "Geografia, Historia y Soberania Nacional 4to", 2, [teachers[8]]),
    Subject(32, "Geografia, Historia y Soberania Nacional 5to", 2, [teachers[8]]),
    Subject(33, "Proyecto de Economia Socioproductiva y Tecnologia 1ro Electricidad", 8, [teachers[25]]),
    Subject(34, "Proyecto de Economia Socioproductiva y Tecnologia 1ro Electronica", 8, [teachers[19]]),
    Subject(35, "Proyecto de Economia Socioproductiva y Tecnologia 1ro Telematica", 8, [teachers[23]]),
    Subject(36, "Proyecto de Economia Socioproductiva y Tecnologia 1ro Metalmecanica", 8, [teachers[14]]),
    Subject(37, "Proyecto de Economia Socioproductiva y Tecnologia 1ro Mecanica Termica", 8, [teachers[18]]),
    Subject(38, "Maquinas, Distribucion y Control 1ro", 8, [teachers[25]]),
    Subject(39, "Maquinas, Distribucion y Control 2do", 8, [teachers[24]]),
    Subject(40, "Maquinas, Distribucion y Control 3ro", 8, [teachers[24]]),
    Subject(41, "Maquinas, Distribucion y Control 4to", 10, [teachers[17]]),
    Subject(42, "Maquinas, Distribucion y Control 5to", 10, [teachers[17]]),
    Subject(43, "Telecomunicacion y Control 1ro", 8, [teachers[19]]),
    Subject(44, "Telecomunicacion y Control 2do", 8, [teachers[22]]),
    Subject(45, "Telecomunicacion y Control 3ro", 8, [teachers[19], teachers[23]]),
    Subject(46, "Telecomunicacion y Control 4to", 10, [teachers[28], teachers[31]]),
    Subject(47, "Telecomunicacion y Control 5to", 10, [teachers[21], teachers[28]]),
    Subject(48, "Programacion y Diseno de Software y Redes 1ro", 8, [teachers[23]]),
    Subject(49, "Mantenimiento Maquinas 1ro", 8, [teachers[14]]),
    Subject(50, "Mantenimiento Maquinas 2do", 8, [teachers[20]]),
    Subject(51, "Mantenimiento Maquinas 3ro", 8, [teachers[20]]),
    Subject(52, "Mantenimiento Maquinas 4to", 10, [teachers[16]]),
    Subject(53, "Mantenimiento Maquinas 5to", 10, [teachers[16]]),
    Subject(54, "Sistemas de Refrigeracion, Aire Acondicionado y Calderas 1ro", 8, [teachers[18]]),
    Subject(55, "Sistemas de Refrigeracion, Aire Acondicionado y Calderas 2do", 8, [teachers[27]]),
    Subject(56, "Sistemas de Refrigeracion, Aire Acondicionado y Calderas 3ro", 8, [teachers[27]]),
    Subject(57, "Sistemas de Refrigeracion, Aire Acondicionado y Calderas 4to", 10, [teachers[26]]),
    Subject(58, "Sistemas de Refrigeracion, Aire Acondicionado y Calderas 5to", 10, [teachers[26]]),
    Subject(59, "Orientacion y Vinculacion 1ro y 2do Electricidad", 4, [teachers[24], teachers[25]]),
    Subject(60, "Orientacion y Vinculacion 1ro y 2do Electronica", 4, [teachers[22], teachers[30]]),
    Subject(61, "Orientacion y Vinculacion 1ro y 2do Telematica", 4, [teachers[23]]),
    Subject(62, "Orientacion y Vinculacion 1ro y 2do Metalmecanica", 4, [teachers[20], teachers[30]]),
    Subject(63, "Orientacion y Vinculacion 1ro y 2do Mecanica Termica", 4, [teachers[18], teachers[27]]),
    Subject(64, "Orientacion y Vinculacion 3ro a 5to Electricidad", 2, [teachers[5], teachers[24]]),
    Subject(65, "Orientacion y Vinculacion 3ro a 5to Electronica", 2, [teachers[5], teachers[18], teachers[19]]),
    Subject(66, "Orientacion y Vinculacion 3ro a 5to Metalmecanica", 2, [teachers[16], teachers[18]]),
    Subject(67, "Orientacion y Vinculacion 3ro a 5to Mecanica Termica", 2, [teachers[5], teachers[18], teachers[30]]),
    Subject(68, "Educacion en Valores 1ro", 2, [teachers[33]]),
    Subject(69, "Educacion en Valores 2do", 2, [teachers[33]]),
    Subject(70, "Educacion en Valores 3ro", 2, [teachers[33]]),
    Subject(71, "Educacion en Valores 4to", 2, [teachers[32]]),
    Subject(72, "Educacion en Valores 5to", 2, [teachers[32]]),
    Subject(73, "Proyecto de Economia Socioproductiva y Tecnologia 2do Electricidad", 8, [teachers[24]]),
    Subject(74, "Proyecto de Economia Socioproductiva y Tecnologia 3ro Electricidad", 8, [teachers[24]]),
    Subject(75, "Proyecto de Economia Socioproductiva y Tecnologia 4to Electricidad", 8, [teachers[17]]),
    Subject(76, "Proyecto de Economia Socioproductiva y Tecnologia 5to Electricidad", 8, [teachers[17]]),
    Subject(77, "Proyecto de Economia Socioproductiva y Tecnologia 2do Electronica", 8, [teachers[22]]),
    Subject(78, "Proyecto de Economia Socioproductiva y Tecnologia 3ro Electronica", 8, [teachers[19], teachers[23]]),
    Subject(79, "Proyecto de Economia Socioproductiva y Tecnologia 4to Electronica", 8, [teachers[31]]),
    Subject(80, "Proyecto de Economia Socioproductiva y Tecnologia 5to Electronica", 8, [teachers[21], teachers[28]]),
    Subject(81, "Proyecto de Economia Socioproductiva y Tecnologia 2do Metalmecanica", 8, [teachers[20]]),
    Subject(82, "Proyecto de Economia Socioproductiva y Tecnologia 3ro Metalmecanica", 8, [teachers[20]]),
    Subject(83, "Proyecto de Economia Socioproductiva y Tecnologia 4to Metalmecanica", 8, [teachers[16]]),
    Subject(84, "Proyecto de Economia Socioproductiva y Tecnologia 5to Metalmecanica", 8, [teachers[16]]),
    Subject(85, "Proyecto de Economia Socioproductiva y Tecnologia 2do Mecanica Termica", 8, [teachers[27]]),
    Subject(86, "Proyecto de Economia Socioproductiva y Tecnologia 3ro Mecanica Termica", 8, [teachers[27]]),
    Subject(87, "Proyecto de Economia Socioproductiva y Tecnologia 4to Mecanica Termica", 8, [teachers[18]]),
    Subject(88, "Proyecto de Economia Socioproductiva y Tecnologia 5to Mecanica Termica", 8, [teachers[26]]),
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
    Group(1, "1ro Electricidad A", [subjects[0], subjects[5], subjects[10], subjects[15], subjects[18], subjects[27], subjects[32], subjects[37], subjects[58], subjects[67]]),
    Group(2, "1ro Electronica A", [subjects[0], subjects[5], subjects[10], subjects[15], subjects[18], subjects[27], subjects[33], subjects[42], subjects[59], subjects[67]]),
    Group(3, "1ro Telematica A", [subjects[0], subjects[5], subjects[10], subjects[15], subjects[18], subjects[27], subjects[34], subjects[47], subjects[60], subjects[67]]),
    Group(4, "1ro Metalmecanica A", [subjects[0], subjects[5], subjects[10], subjects[15], subjects[18], subjects[27], subjects[35], subjects[48], subjects[61], subjects[67]]),
    Group(5, "1ro Mecanica Termica A", [subjects[0], subjects[5], subjects[10], subjects[15], subjects[18], subjects[27], subjects[36], subjects[53], subjects[62], subjects[67]]),
    Group(6, "2do Electricidad A", [subjects[1], subjects[6], subjects[11], subjects[16], subjects[19], subjects[28], subjects[72], subjects[38], subjects[58], subjects[68]]),
    Group(7, "2do Electronica A", [subjects[1], subjects[6], subjects[11], subjects[16], subjects[19], subjects[28], subjects[76], subjects[43], subjects[59], subjects[68]]),
    Group(8, "2do Electronica B", [subjects[1], subjects[6], subjects[11], subjects[16], subjects[19], subjects[28], subjects[76], subjects[43], subjects[59], subjects[68]]),
    Group(9, "2do Metalmecanica A", [subjects[1], subjects[6], subjects[11], subjects[16], subjects[19], subjects[28], subjects[80], subjects[49], subjects[61], subjects[68]]),
    Group(10, "2do Mecanica Termina A", [subjects[1], subjects[6], subjects[11], subjects[16], subjects[19], subjects[28], subjects[84], subjects[54], subjects[62], subjects[68]]),
    Group(11, "3ro Electricidad A", [subjects[2], subjects[7], subjects[12], subjects[17], subjects[20], subjects[21], subjects[29], subjects[73], subjects[39], subjects[63], subjects[69]]),
    Group(12, "3ro Electronica A", [subjects[2], subjects[7], subjects[12], subjects[17], subjects[20], subjects[21], subjects[29], subjects[77], subjects[44], subjects[64], subjects[69]]),
    Group(13, "3ro Electronica B", [subjects[2], subjects[7], subjects[12], subjects[17], subjects[20], subjects[21], subjects[29], subjects[77], subjects[44], subjects[64], subjects[69]]),
    Group(14, "3ro Metalmecanica A", [subjects[2], subjects[7], subjects[12], subjects[17], subjects[20], subjects[21], subjects[29], subjects[81], subjects[50], subjects[65], subjects[69]]),
    Group(15, "3ro Mecanica Termina A", [subjects[2], subjects[7], subjects[12], subjects[17], subjects[20], subjects[21], subjects[29], subjects[85], subjects[55], subjects[66], subjects[69]]),
    Group(16, "4to Electricidad A", [subjects[3], subjects[8], subjects[13], subjects[22], subjects[23], subjects[24], subjects[30], subjects[74], subjects[40], subjects[63], subjects[70]]),
    Group(17, "4to Electronica A", [subjects[3], subjects[8], subjects[13], subjects[22], subjects[23], subjects[24], subjects[30], subjects[78], subjects[45], subjects[64], subjects[70]]),
    Group(18, "4to Electronica B", [subjects[3], subjects[8], subjects[13], subjects[22], subjects[23], subjects[24], subjects[30], subjects[78], subjects[45], subjects[64], subjects[70]]),
    Group(19, "4to Metalmecanica A", [subjects[3], subjects[8], subjects[13], subjects[22], subjects[23], subjects[24], subjects[30], subjects[82], subjects[51], subjects[65], subjects[70]]),
    Group(20, "4to Mecanica Termina A", [subjects[3], subjects[8], subjects[13], subjects[22], subjects[23], subjects[24], subjects[30], subjects[86], subjects[56], subjects[66], subjects[70]]),
    Group(21, "5to Electricidad A", [subjects[4], subjects[9], subjects[14], subjects[25], subjects[26], subjects[31], subjects[75], subjects[41], subjects[63], subjects[71]]),
    Group(22, "5to Electronica A", [subjects[4], subjects[9], subjects[14], subjects[25], subjects[26], subjects[31], subjects[79], subjects[46], subjects[64], subjects[71]]),
    Group(23, "5to Electronica B", [subjects[4], subjects[9], subjects[14], subjects[25], subjects[26], subjects[31], subjects[79], subjects[46], subjects[64], subjects[71]]),
    Group(24, "5to Metalmecanica A", [subjects[4], subjects[9], subjects[14], subjects[25], subjects[26], subjects[31], subjects[83], subjects[52], subjects[65], subjects[71]]),
    Group(25, "5to Mecanica Termina A", [subjects[4], subjects[9], subjects[14], subjects[25], subjects[26], subjects[31], subjects[87], subjects[57], subjects[66], subjects[71]]),
]

def random_start_hour(duration: int) -> int:
    day = random.randint(0, 4)
    day_start = (day * 10) + 1
    return random.randint(day_start, (day_start + 10) - duration)

def is_teacher_available(teacher, start_hour: int, duration: int) -> bool:
    teacher = next((t for t in teachers if t.id == teacher), None)

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
    physic_education = [16, 17, 18]

    for event in events:
        if event.group not in groups_block:
            groups_block[event.group] = set()

        if event.teacher not in teachers_block:
            teachers_block[event.teacher] = set()

        found_block = False
        start_hour = random_start_hour(event.duration)

        for _ in range(100):
            event_hours = range(start_hour, start_hour + event.duration)

            if (not groups_block[event.group].intersection(event_hours) and 
                not teachers_block[event.teacher].intersection(event_hours) and 
                is_teacher_available(event.teacher, start_hour, event.duration)):
                
                event.start_hour = start_hour
                if event.subject not in physic_education:
                    event.room = random.choice(rooms).id

                groups_block[event.group].update(event_hours)
                teachers_block[event.teacher].update(event_hours)
                found_block = True
                break

            start_hour = move_hour(start_hour, event.duration)

        if not found_block:
            start_hour = random_start_hour(event.duration)
            for _ in range(100):
                event_hours = range(start_hour, start_hour + event.duration)
                
                if not groups_block[event.group].intersection(event_hours) and is_teacher_available(event.teacher, start_hour, event.duration):
                    event.start_hour = start_hour
                    if event.subject not in physic_education:
                        event.room = random.choice(rooms).id
                    groups_block[event.group].update(event_hours)
                    teachers_block[event.teacher].update(event_hours) 
                    found_block = True
                    break

                start_hour = move_hour(start_hour, event.duration)
            
            if not found_block:
                possible_hours = []
                teacher_obj = next((t for t in teachers if t.id == event.teacher), None)

                if teacher_obj:
                    for av in teacher_obj.availabilities:
                        for h in range(av.start_hour, (av.end_hour - event.duration) + 2):
                            possible_hours.append(h)
                
                if possible_hours:
                    event.start_hour = random.choice(possible_hours)
                else:
                    event.start_hour = random_start_hour(event.duration)

                if event.subject not in physic_education:
                    event.room = random.choice(rooms).id

                event_hours = range(event.start_hour, event.start_hour + event.duration)
                groups_block[event.group].update(event_hours)
                teachers_block[event.teacher].update(event_hours)

        timetable.append(event)
    
    return timetable

def create_events():
    project_ids = [*range(33, 38), *range(73, 89)]
    event_list = []
    id = 1

    for group in groups:
        sorted_subjects = sorted(group.subjects, key=lambda s: s.hours, reverse=True)

        for subject in sorted_subjects:
            left_hours = subject.hours
            teacher = random.choice(subject.teachers)

            while left_hours > 0:
                if left_hours > 2 and left_hours < 8:
                    if left_hours == 4:
                        duration = 2
                    else:
                        duration = random.randint(2, left_hours)

                elif subject.id in project_ids and left_hours == 8:
                    even_hours = [6, 8]
                    duration = random.choice(even_hours)

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
        # Extraemos solo el score numérico desestimando las listas de fallas con ', _'
        g_score, _ = groups_subjects(individual)
        t_score, _ = teachers_subjects(individual)
        r_score = rooms_groups(individual) # Esta quedó igual que antes
        gap_score, _ = groups_gaps(individual)
        sub_score, _ = subject_day(individual)
        
        total_score = g_score + t_score + r_score + gap_score + sub_score
        results.append(total_score)

    return results
        

def groups_subjects(individual: list[Event]):
    score = 0
    groups_occupation = {}
    collisions = []

    for event in individual:
        if event.start_hour is None:
            continue
        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.group, block)

            if key in groups_occupation:
                existing_event = groups_occupation[key]
                score += 200
                collisions.append({
                    "group": event.group,
                    "block": block,
                    "event_1": {"id": existing_event.id, "subject": existing_event.subject},
                    "event_2": {"id": event.id, "subject": event.subject}
                })
            else:
                groups_occupation[key] = event
    
    return score, collisions

def teachers_subjects(individual: list[Event]):
    score = 0
    teachers_occupation = {}
    collisions = [] 
    # Conjunto para rastrear choques conceptuales únicos ya penalizados
    # Guardará tuplas de (teacher_id, min_event_id, max_event_id)
    penalized_pairs = set()

    for event in individual:
        if event.start_hour is None:
            continue

        for block in range(event.start_hour, event.start_hour + event.duration):
            key = (event.teacher, block)

            if key in teachers_occupation:
                existing_event = teachers_occupation[key]
                
                # Identificadores ordenados para evitar contar (A, B) y (B, A) como diferentes
                event_pair = (event.teacher, min(existing_event.id, event.id), max(existing_event.id, event.id))
                
                # Solo sumamos al score de fitness si es la primera vez que detectamos este choque de eventos
                if event_pair not in penalized_pairs:
                    score += 150
                    penalized_pairs.add(event_pair)
                
                    # Opcional: El reporte detallado puede seguir mostrando todos los bloques 
                    # o puedes filtrarlo aquí para que solo guarde una colisión conceptual.
                    # Mantenerlo aquí registrará cada bloque; si prefieres un reporte compacto, 
                    # puedes meter este append dentro del 'if event_pair not in penalized_pairs:'
                    collisions.append({
                        "teacher_id": event.teacher,
                        "block": block,
                        "event_1": {
                            "id": existing_event.id,
                            "subject": existing_event.subject,
                            "group": existing_event.group
                        },
                        "event_2": {
                            "id": event.id,
                            "subject": event.subject,
                            "group": event.group
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
                key = (event.room, block)

                if key in rooms_occupation:
                    score += 0 # 0 temporalmente hasta que sepa como se manejan los salones
                else:
                    rooms_occupation[key] = event
    
    return score

def groups_gaps(individual: list[Event]):
    score = 0
    timetable_map = {}
    gaps_report = []

    for event in individual:
        if event.start_hour is None:
            continue
        for block in range(event.start_hour, event.start_hour + event.duration):
            day = (block - 1) // 10
            hour_in_day = ((block - 1) % 10) + 1
            
            if event.group not in timetable_map:
                timetable_map[event.group] = {d: set() for d in range(5)}
                
            timetable_map[event.group][day].add(hour_in_day)

    for group, days in timetable_map.items():
        for day, occupied_hours in days.items():
            if not occupied_hours:
                continue
            
            first_hour = min(occupied_hours)
            last_hour = max(occupied_hours)
            gaps_count = 0
            specific_hours = []

            for h in range(first_hour, last_hour + 1):
                if h not in occupied_hours:
                    gaps_count += 1
                    specific_hours.append(h)
            
            if gaps_count > 0:
                if first_hour > 1:
                    score += gaps_count * 80
                    gaps_report.append({
                        "group": group,
                        "day": day,
                        "type": "Entrada tarde con baches (No permitido)",
                        "gaps_count": gaps_count,
                        "hours": specific_hours
                    })
                else:
                    max_allowed_gaps = 2
                    if gaps_count > max_allowed_gaps:
                        score += (gaps_count - max_allowed_gaps) * 40
                        gaps_report.append({
                            "group": group,
                            "day": day,
                            "type": f"Exceso de horas libres (Permitido: {max_allowed_gaps})",
                            "gaps_count": gaps_count,
                            "hours": specific_hours
                        })
    return score, gaps_report

def subject_day(individual: list[Event]):
    score = 0
    group_day_subjects = {}
    subject_duplications = []

    for event in individual:
        if event.start_hour is None:
            continue
        
        day = (event.start_hour - 1) // 10
        
        if event.group not in group_day_subjects:
            group_day_subjects[event.group] = {d: {} for d in range(5)}
            
        # Si la materia ya fue registrada este día, guardamos la falla
        if event.subject in group_day_subjects[event.group][day]:
            score += 175
            existing_event_id = group_day_subjects[event.group][day][event.subject]
            subject_duplications.append({
                "group": event.group,
                "day": day,
                "subject": event.subject,
                "event_1_id": existing_event_id,
                "event_2_id": event.id
            })
        else:
            group_day_subjects[event.group][day][event.subject] = event.id

    return score, subject_duplications

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
    physic_education = [16, 17, 18]

    for event in individual:
        if random.random() < 0.02:
            current_subject = next((s for s in subjects if s.id == event.subject), None)
            available_teachers = []
            if current_subject:
                # 1. Encontrar todos los bloques horarios actuales de esta materia para este grupo
                # (Ya que al cambiar de profesor, se le cambiarán TODOS sus bloques asignados)
                current_blocks_of_subject = []
                for e in individual:
                    if e.subject == event.subject and e.group == event.group and e.start_hour is not None:
                        current_blocks_of_subject.append((e.start_hour, e.duration))
                
                # 2. Filtrar profesores candidatos
                for t in current_subject.teachers:
                    if t.id == event.teacher:
                        continue
                    
                    # Verificamos si este profesor está disponible en TODOS los bloques de la materia
                    is_available_for_all = True
                    for start_h, duration in current_blocks_of_subject:
                        if not is_teacher_available(t.id, start_h, duration):
                            is_available_for_all = False
                            break # Con un bloque en el que no pueda, queda descartado
                    
                    if is_available_for_all:
                        available_teachers.append(t)

            # DECISIÓN INTELIGENTE: Si hay profesores alternativos, tiramos una moneda (50/50).
            # Si el profesor es ÚNICO, lo obligamos a ir directamente a MUTAR HORA.
            mutar_profesor = False
            if available_teachers and random.choice([True, False]):
                mutar_profesor = True

            if mutar_profesor:
                # --- MUTAR PROFESOR ---
                new_teacher = random.choice(available_teachers)
                i_subject = event.subject
                i_group = event.group

                for e in individual:
                    if e.group > i_group:
                        break
                    if e.subject == i_subject and e.group == i_group:
                        e.teacher = new_teacher.id
                    
            else:
                # --- MUTAR HORA ---
                taken_hours = set()

                # CORRECCIÓN CRÍTICA: Bloqueamos las horas donde el grupo YA tiene clases
                # Y TAMBIÉN las horas donde este profesor YA está dictando otra clase en el instituto
                for e in individual:
                    if e.id != event.id and e.start_hour is not None:
                        # Si es del mismo grupo O es el mismo profesor, esa hora NO está disponible
                        if e.group == event.group or e.teacher == event.teacher:
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
                    teacher_obj = next((t for t in teachers if t.id == event.teacher), None)
                    
                    if teacher_obj:
                        for av in teacher_obj.availabilities:
                            for h in range(av.start_hour, (av.end_hour - event.duration) + 2):
                                valid_hours_for_prof.append(h)
                                
                    if valid_hours_for_prof:
                        event.start_hour = random.choice(valid_hours_for_prof)
        else:
            if random.random() < 0.01 and event.subject not in physic_education:
                event.room = random.choice(rooms).id
    
    return individual

def main():
    events = create_events()
    i = 0
    population = create_population(50, events)

    while i < 2000:
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
    best_timetable = selected_population[0][1] # O como extraigas tu mejor individuo de la población

    # Generamos el reporte completo de auditoría
    final_report = evaluate_and_report(best_timetable)

    # --- IMPRESIÓN DEL REPORTE FINAL DE FALLAS ---
    print("\n" + "="*50)
    print(f" AUDITORÍA DE CALIDAD DEL HORARIO (Fitness Final: {final_report['total_fitness']})")
    print("="*50)

    print(f"\n[!] Choques de Grupos Detectados: {len(final_report['group_collisions'])}")
    for fail in final_report['group_collisions']:
        print(f"  - Grupo {fail['group']} en Bloque {fail['block']}: Conflicto entre Evento {fail['event_1']['id']} ({fail['event_1']['subject']}) y Evento {fail['event_2']['id']} ({fail['event_2']['subject']})")

    print(f"\n[!] Choques de Profesores Detectados: {len(final_report['teacher_collisions'])}")
    for fail in final_report['teacher_collisions']:
        print(f"  - Profesor {fail['teacher_id']} en Bloque {fail['block']}: Evento {fail['event_1']['id']} (Grupo {fail['event_1']['group']}) choca con Evento {fail['event_2']['id']} (Grupo {fail['event_2']['group']})")

    print(f"\n[!] Baches y Ventanas Horarias de Alumnos: {len(final_report['gaps'])}")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    for fail in final_report['gaps']:
        print(f"  - Grupo {fail['group']} ({dias_semana[fail['day']]}): {fail['type']}. Tiene {fail['gaps_count']} horas muertas en los bloques internos: {fail['hours']}.")

    print(f"\n[!] Materias Repetidas el Mismo Día: {len(final_report['subject_duplications'])}")
    for fail in final_report['subject_duplications']:
        print(f"  - Grupo {fail['group']} ({dias_semana[fail['day']]}): La materia {fail['subject']} se imparte de forma fragmentada en los Eventos {fail['event_1_id']} y {fail['event_2_id']}.")

    print("\n" + "="*50)

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

def evaluate_and_report(best_individual: list[Event]):
    """
    Ejecuta las funciones en el mejor individuo al final de las generaciones
    para compilar el informe definitivo de fallas y baches.
    """
    g_score, group_collisions = groups_subjects(best_individual)
    t_score, teacher_collisions = teachers_subjects(best_individual)
    gap_score, gaps_report = groups_gaps(best_individual)
    sub_score, subject_duplications = subject_day(best_individual)
    
    report = {
        "total_fitness": g_score + t_score + gap_score + sub_score,
        "group_collisions": group_collisions,
        "teacher_collisions": teacher_collisions,
        "gaps": gaps_report,
        "subject_duplications": subject_duplications
    }
    return report

if __name__ == "__main__":
    main()

