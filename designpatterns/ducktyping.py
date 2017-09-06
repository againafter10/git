# duck typing
#  duck typing requires that type checking be deferred to runtime, and is implemented by means of dynamic typing or reflection.

class Sparrow:
    def fly(self):
        print("Sparrow flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()

sparrow = Sparrow()
airplane = Airplane()
whale = Whale()

lift_off(sparrow) 
lift_off(airplane) 
lift_off(whale)