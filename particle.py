
import math

K_CONSTANT = 8.99e+9


class Particle:
    def __init__(self, x_pos, y_pos, charge):
        self.pos = [x_pos, y_pos]
        self.charge = charge

    def electric_field_at(self, x:float, y:float) -> list[float, float]:
        return K_CONSTANT * self.charge / (self.distance_to(x, y)**2)

    def distance_to(self, x:float, y:float) -> float:
        return math.sqrt((x - self.pos[0])**2 + (y - self.pos[1])**2)