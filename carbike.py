from democlass import vehical,Bike,Car

car1 = Car()
car1.start()
car1.stop()
car1.start().stop()
bike1 = Bike()
bike1.start().stop()
num = 17
list = [1,3,6,8]
def set_color(object,color):
    object.color = color
set_color(car1,"blue")
print(car1.color)
def set_color(Bike,color):
    Bike.color = color
set_color(Bike,"red")
print(bike1.color)


