
from copy import deepcopy

class Prototype(object):

    def clone(self):
        return deepcopy(self)


class ConcretePrototype1(Prototype):

     def __init__(self):
        self.name = 'Bear'


class ConcretePrototype2(Prototype):

    def __init__(self):
        self.name = 'Bull'

c1 = ConcretePrototype1()
c2 = ConcretePrototype2()
c1c = c1.clone()
c2c = c2.clone()
