from itertools import cycle
import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    @staticmethod
    def running():
        for _ in cycle(TrafficLight.__color):
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(5)


traffic_light = TrafficLight()
traffic_light.running()
