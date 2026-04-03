import time
class traficlights:
    @staticmethod
    def stop():
        print("red light")
        time.sleep(5)
    @staticmethod
    def ready():
        print("yellow light")
        time.sleep(3.3)
    @staticmethod
    def start():
        print("green light")
        time.sleep(10)
