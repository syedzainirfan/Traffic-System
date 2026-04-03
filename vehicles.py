class objects:
    def __init__(self,vehicles_id,vehicles_type):
        self.vehicles_id=vehicles_id
        self.vehicles_type=vehicles_type
        self.position=0
        self.state="Stopped"
    def move(self):
        self.state="Moving"
        self.position+=1
        return f"{self.vehicles_id}{self.vehicles_type} is moving ....position is {self.position}"
    def stopped(self):
        self.state="stopped"
        return f"{self.vehicles_id}{self.vehicles_type} is moving ....position is {self.position}"