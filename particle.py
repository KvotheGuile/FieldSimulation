
import math

K_CONSTANT = 8.99e+9


class Particle:
    def __init__(self, x_pos, y_pos, charge):
        self.pos = [x_pos, y_pos]
        self.charge = charge

    def electric_field_at(self, point:list[float]) -> list[float]:
        distance: float = self.distance_to(point[0], point[1])
        if distance == 0: return [0, 0]

        magnitude: float = K_CONSTANT * self.charge / (distance**2)
        direction: list[float] = self.direction_to(point)
        return [magnitude * direction[0], magnitude * direction[1]]

    def direction_to(self, point: list[float]) -> list[float]:
        disp: list[float] = [point[0] - self.pos[0], point[1] - self.pos[1]]
        magnitude: float = self.distance_to(point[0], point[1])

        if magnitude == 0: return [0, 0]

        return [disp[0]/magnitude, disp[1]/magnitude]

    def distance_to(self, x:float, y:float) -> float:
        return math.sqrt((x - self.pos[0])**2 + (y - self.pos[1])**2)