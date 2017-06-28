#!/usr/bin/env python
  
class calculator:

    def __init__(self, ina, inb):
        self.a = ina
        self.b = inb

    def add(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b

class scientific(calculator):
    def power(self):
        return pow(self.a, self.b)

newCal = calculator(10,20)

print "a + b: %d" % newCal.add()
print "a * b: %d" % newCal.mult()

newPower = scientific(2,3)

print "a + b: %d" % newPower.add()
print "a * b: %d" % newPower.mult()

print "a pow b: %d" % newPower.power()
