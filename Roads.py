class Ways:

    def __init__(self, road_ways: list):
        self.road_ways = road_ways
        self.GO = "Start"
        self.STOP = "Stop"

    def intersection(self, activate):
        status = {}

        for x in self.road_ways:
            if x == activate:
                status[x] = "Green Light"
            else:
                status[x] = "Red Light"

        return status
