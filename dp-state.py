import time

class Red:
    def change(self, light):
        print("紅燈")
        time.sleep(5)
        light.set(Green())

class Green:
    def change(self, light):
        print("綠燈")
        time.sleep(5)
        light.set(Yellow())

class Yellow:
    def change(self, light):
        print("黃燈")
        time.sleep(1)
        light.set(Red())

class TrafficLight:
    def __init__(self):
        self.current = Red()
    
    def set(self, state):
        self.current = state
    
    def change(self):
        self.current.change(self)
        
trafficLight = TrafficLight()
while True:
    trafficLight.change()