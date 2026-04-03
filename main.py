from event_system import system
from trafic_lights import traficlights
from vehicles import objects
from roads import Ways

if __name__ == "__main__":
    roads = Ways(["North", "South", "East", "West"])
    car1 = objects("001", "Car")
    bus1=objects("002","bus")
    traffic_system = system(roads)
    traffic_system.event()
    print(car1.move())
    print(bus1.move())



"""
2D grid (0,0) to (1000,1000)
Point A to Point B
Point A is Car's Initial position for example (0,0)
Point B is Destination for example (100, 0)
Car 1 sec per coordinate (0,0) -> (1,0) => 1 sec
5 Signals (Green, Red, Green, Red, Red) (20,0) (40,0) (50,0) (60,0) (80,0)
Green -> 10 sec Red
Red -> 30 sec Green
Total Seconds Point A to Point B
"""