#! /usr/bin/env python

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getFirstname(self):
      return(self.firstname)

    def getLastname(self):
        return(self.lastname)

    #Return the full name of the person
    def __str__(self):
        return "The name of the person is %s %s." % (self.firstname, self.lastname)

#Add class called Student that inherit from the Person class
class Student(Person):
    def __init__(self, firstname, lastname, subject_area):
      Person.__init__(self, firstname, lastname)
      self.subject_area = subject_area
     
    def printNameSubject(self):
        return(self.firstname, self.lastname, self.subject_area)

#Add another class Techer that also inherit from Person class
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
      Person.__init__(self, firstname, lastname)
      self.course = course

    def printTeacherCourse(self):
        return(self.firstname, self.lastname, self.course)
