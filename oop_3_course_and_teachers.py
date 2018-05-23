# У меня не очень получилось, если честно

from abc import ABCMeta, abstractmethod
import os

class Person:
    name = 'name'
    age = 0
    course = 'Python'

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


class Students(Person):
    student = 'student'
    grades = 0

    def make_student(Person, name, age, course, grades):
        student.set (Person, name, age, course)


        def set_grades(self, grades):
            self.grades = grades
            student.grades = grades


Vova = Students()
Vova.make_student("Vova", 20, "Python", 4)
