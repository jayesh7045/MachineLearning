import sys;
class car:
    pass
audi = car()
bmw = car()
print(type(audi))
print(type(bmw))
audi.windows = 4;
print(audi.windows)
print(type(car))
print(sys.getsizeof(car))
print(sys.getsizeof(4))