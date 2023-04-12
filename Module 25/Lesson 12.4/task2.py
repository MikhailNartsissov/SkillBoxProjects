class CanFly:
    def __init__(self, c_height=0, c_speed=0):
        self.height = c_height
        self.speed = c_speed

    def take_off(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return self.height, self.speed


class Butterfly(CanFly):
    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):
    def take_off(self):
        self.speed = 500
        self.height = 1000

    def explode(self):
        self.speed = 0
        print('Бум!')

    def land(self):
        self.height = 0
        self.explode()


butterfly = Butterfly()
butterfly.take_off()
butterfly.fly()
print(butterfly.__str__())

rocket = Rocket()
rocket.take_off()
print(rocket.__str__())
rocket.land()
