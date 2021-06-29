def add(*args):
    #print(args[1])

    sum = 0
    for n in args:
        sum += n 
    return sum 


#print(add(2, 4, 6, 8, 9))

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.make)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
print(all_aboard(4, 7, 3, 0, x=10, y=64))