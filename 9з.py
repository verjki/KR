import numpy

class Student:

    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.grades = grades

    def greeting(self):
        return 'Hello, I am Student', self.fullname

    def mean_grade(self):
        mean = numpy.average(self.grades)
        return mean

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, second):
        return f'{self.name} is friends with {second.name}'

    def __str__(self):
        return self.fullname


