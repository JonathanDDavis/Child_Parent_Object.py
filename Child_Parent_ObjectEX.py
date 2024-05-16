#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     22/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Person:
    def _init_(self, fname, lname, ssn):
        self.firstname=fname
        self.lastname= lname
        self.ssn = ssn

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe", "123-45-6789")
x.printname()

class Student(Person):
##    def printssn(self):
##        print(self.ssn)
    pass

y = Student("Sally", "Student", "123-45-6789")
##y.printssn()
y.printname()
