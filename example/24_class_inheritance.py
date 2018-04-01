#!/usr/bin/python

class Car:
    "Base class of car"
    
    performance = "normal"
    brand = ""
    price = 0

    def __init__(self):
        print "Calling base-class"
    
    def setBrand(self, brand):
        Car.brand = brand

    def getBrand(self):
        return Car.brand

    def getPrice(self):
        print Car.price
        return Car.price

    def setPerformance(self, speed):
        Car.performance = speed

class Benz(Car):
    "Benz sub-class"

    def __init__(self):
        print "Calling sub-class"

benzObj = Benz()
benzObj.setBrand("Benz")
print benzObj.getBrand()
