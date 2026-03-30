from traffic_lights import trafficlights
from vehicles import objects
from roads import Ways


class system:
    
    def __init__(self, ways):
        self.ways = ways
        self.activate = "North"

    def event(self):
        result = self.ways.intersection(self.activate)

        if result[self.activate] == "Green light":
            return trafficlights.start()
        else:
            return trafficlights.stop()
