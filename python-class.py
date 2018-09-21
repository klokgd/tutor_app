class Vehicle(object):
    """docstring"""
    mark = "mitsubisi"
    color = "cool color"
    wheels = "99"
    passanger = "1000"

    def changemark(self, newmark):
         self.mark = newmark

    def changecolor(self, newcolor):
         self.color = newcolor

    def changewheels(self, countwheels):
         self.wheels = countwheels

    def changepassanger(self, newpassanger):
         self.passanger = newpassanger


obj1 = Vehicle()
obj2 = Vehicle()
obj3 = Vehicle()

print(obj1.color, obj1.mark, obj1.passanger, obj1.wheels)
print(obj2.color, obj2.mark, obj2.passanger, obj2.wheels)


obj3.changecolor("huesoskii cvet")
obj3.changewheels("ne skazhu")
obj3.changemark("pizda tvoei mamy")
obj3.changepassanger("0")

print(obj3.color, obj3.mark, obj3.passanger, obj3.wheels)
