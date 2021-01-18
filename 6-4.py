class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = is_police

    def go(self):
        return f'{self.name} car started moving'

    def stop(self):
        return f'{self.name} car stopped'

    def turn_right(self):
        return f'{self.name} car turned right'

    def turn_left(self):
        return f'{self.name} car turned left'

    def show_speed(self):
        return f'{self.name} car current speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Excess speed! Your speed is {self.speed}'
        else:
            return f'{self.name} car current speed is {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Excess speed! Your speed is {self.speed}'
        else:
            return f'{self.name} car current speed is {self.speed}'


class PoliceCar(Car):
    pass


car_1 = TownCar(60, 'Black', 'Kia', False)
print(car_1.go())
print(car_1.stop())
print(car_1.turn_left())
print(car_1.show_speed())
