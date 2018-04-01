#!/usr/bin/python

class Employee:
    "Employee class"
    empCount = 0

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def getEmpCount(self):
        return Employee.empCount

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getFullProfile(self, company):
        return "Your fullname is %s %s" %(self.getName(), company) 

# Instance the object
golf = Employee("Teerapong", 100000)        
print golf.getEmpCount()
print golf.getSalary()
print golf.getFullProfile("AXA")