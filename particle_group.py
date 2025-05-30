
from particle import Particle
import math as m

class ParticleManager:
    def __init__(self):
        self.particles: list[Particle] = []

    def electric_field_x(self, x: float, y: float) -> float:
        vec = self.electric_field_at_point([x, y])
        return vec[0]

    def electric_field_y(self, x: float, y: float) -> float:
        vec = self.electric_field_at_point([x, y])
        return vec[1]

    def electric_field_at_point(self, point: list[float]) -> list[float]:
        field_total = [0, 0]

        if len(self.particles) < 1:
            return field_total

        for particle_i in self.particles:
            if not self.close_enough(point, particle_i.pos):
                field_i = particle_i.electric_field_at(point)
                # print(f"{field_total} + {field_i} = ", end='')
                field_total = [field_total[0] + field_i[0],
                               field_total[1] + field_i[1]]
                # print(f"{field_total}")

        magnitude = m.sqrt(field_total[0] ** 2 + field_total[1] ** 2)
        # print(magnitude)

        if magnitude > 2e-10:
            field_total = [field_total[0]/magnitude, field_total[1]/magnitude]
            if magnitude > 5e-10:
                field_total = [field_total[0] * 1.5, field_total[1] * 1.5]

        return field_total

    def add_particle(self, new_particle: Particle) -> None:
        self.particles.append(new_particle)

    @staticmethod
    def close_enough(point_A, point_B, margin=0.01) -> bool:
        magnitude = m.sqrt((point_A[0] - point_B[0])**2 + (point_A[1] - point_B[1])**2)
        return magnitude < margin
