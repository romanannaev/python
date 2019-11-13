class Persona:
    age = 0
    def __init__(self, name, date, tdate ):
        self.name = name
        self.date = date
        self.tdate = tdate


    def Age(self):
        self.age = self.tdate - self.date



    def info(self):
        self.Age()
        print('Создан объект класса Person')
        return print(('Фамилия Имя:' "{0}" "  " 'Возраст'"  " "{1}").format(self.name, self.age))




#pers = Persona("Alex Ivanov",1960,2009)
#pers.Age()
#print(pers.age)
#pers.info()

#per = Persona('Alex Ivanov', 1983, 2019)
#print(per.info())

class Abiturient(Persona):
    def __init__(self, name, date, tdate, faculty):
        super().__init__(name, date, tdate)
        self.faculty = faculty

    def info(self):
        Persona.Age(self)
        Persona.info(self)
        print('Создан объект класса Abiturient')
        return ('Факультет :' "{0}").format(self.faculty)

#abit = Abiturient("Alex Ivanov", 1998, 2019, 'УПП')


#print(abit.info())


class Student(Persona):
    def __init__(self, name, date, tdate, faculty, course):
        super().__init__(name, date, tdate)
        self.faculty = faculty
        self.course = course
    def info(self):
        Persona.Age(self)
        Persona.info(self)
        print('Создан объект класса Student')
        return ('Факультет : "{0}"; Курс : "{1}"').format(self.faculty, self.course)


#stu = Student("Oleg Gut", 1993, 2019, "УПП", 5)
#print(stu.info())

class Prepodavatel(Persona):
    def __init__(self, name, date, tdate, faculty, dolgnost, staj):
        super().__init__(name, date, tdate)
        self.faculty = faculty
        self.dolgnost = dolgnost
        self.staj = staj

    def info(self):
        Persona.Age(self)
        Persona.info(self)
        print("Создан субъект класса Преподаватель")
        return ('Факультет : "{0}" Должность :"{1}" Стаж : "{2}"').format(self.faculty, self.dolgnost, self.staj)

#prep = Prepodavatel("Петр Петров", 1956, 2019, "УПП","Проффесор", 30)
#print(prep.info())

#--------Основная часть программы-------------

itogspisok = []

n = int(input("Введите количество персон: "))
tdate1 = int(input("Введите текущий год: "))

for i in range(n):
    persona = input("KTO вы? 1) Абитуриент, 2) Студент, 3) Преподаватель) ")
    name1 = input("Bведите вашу фамилию и имя: ")
    date1 = int(input("Bвeдитe год рождения: "))
    spisok=[name1, date1]
    itogspisok.append(spisok)

#print(itogspisok)

    if persona == '1':
        faculty1 = input("Bведите факультет: ")

        abitur = Abiturient(name1, date1, tdate1, faculty1)

        print(abitur.info())

        print()

    if persona == "2":

        faculty1 = input("Bведите факультет: ")
        course1 = int(input("Введите курс: "))
        stud = Student(name1, date1, tdate1, faculty1, course1)
        print(stud.info())
        print()

    if persona == "3":
        faculty1 = input("Введите факультет: ")
        dolgnost1 = input("Bвeдитe должность: ")
        staj1 = input("Введите стаж работы: ")

        prepod = Prepodavatel(name1, date1, tdate1, faculty1, dolgnost1, staj1)

        print(prepod.info())

print("Далее будут отобраны персоны, чей год рождения попадает в заданный промежуток")

print(itogspisok)
diapazon1 = int(input("Введите начало промежутка: "))
diapazon2 = int(input("Введите конец промежутка: "))
print(" персоны, удовлетворяющие заданному условию:")
for i in range(len(itogspisok)):
    if (itogspisok[i][1] >= diapazon1) and (itogspisok[i][1] <= diapazon2):
        print("Фамилия Имя: ", itogspisok[i][0], "Год рождения: ", itogspisok[i][1])




