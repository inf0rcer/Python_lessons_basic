# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import random

Surname = ('Сидоров', 'Иванов', 'Петров', 'Осин', 'Волин', 'Сергеев', 'Дмитриев', 'Турин', 'Ткачев', 'Захаров', 'Лунев')
Name = ('Ф.', 'А.', 'Д.', 'С.', 'Л.', 'В.', 'П.', 'Я.', 'Н.', 'Е.')
Subject = ('математика', 'русский язык', 'физика', 'английский язык', 'химия', 'биология')


class School():
    def __init__(self, name):
        self.name = name
        self.Classes = []

    def add_Class(self, Class):
        self.Classes.append(Class)

    def show_Classes(self):
        print('В школе {} есть следующие классы:'.format(self.name))
        for item in self.Classes:
            print('класс {}'.format(item.name))

    def show_Class_Pupils(self, name):
        for item in self.Classes:
            if item.name == name: item.showClassPupils()

    def show_Pupil_Information(self, name):
        for clss in self.Classes:
            for pupil in clss.Pupils:
                if pupil.name == name:
                    for teacher in clss.Teachers:
                        print('Ученик {} Класс {} Преподаватель {} Предмет {}'.format(pupil.name, clss.name, teacher.name,
                                                                                      teacher.subject))

    def show_Pupil_Parents(self, name):
        for clss in self.Classes:
            for pupil in clss.Pupils:
                if pupil.name == name: pupil.showParents()

    def gen_School(self, classes, pupils, subjects):
        for index in range(int(classes)):
            gen_class = Class(str(random.randint(1, 11)) + random.choice(('A', 'B', 'C', 'D')))
            self.addClass(gen_class)
            for i in range(int(pupils)):
                gen_class.addPupil(Pupil(random.choice(Surname) + ' ' + random.choice(Name) + random.choice(Name),
                                      random.choice(Surname) + ' ' + random.choice(Name) + random.choice(Name),
                                      random.choice(Surname) + 'а ' + random.choice(Name) + random.choice(Name)))
            for i in range(int(subjects)):
                gen_class.addTeacher(random.choice(Surname) + random.choice(Name) + random.choice(Name),
                                  random.choice(Subject))


class Class():
    def __init__(self, name):
        self.name = name
        self.Pupils = []
        self.Teachers = []

    def add_Pupil(self, pupil):
        self.Pupils.append(pupil)

    def add_Teacher(self, name, subject):
        self.Teachers.append(Teacher(name, subject))

    def show_Class(self):
        print('В классе {} есть следующие ученики:'.format(self.name))
        for item in self.Pupils:
            print('ученик {}'.format(item.name))


class Pupil():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def showParents(self):
        print('Родители: {}, {}'.format(self.father, self.mother))


class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject