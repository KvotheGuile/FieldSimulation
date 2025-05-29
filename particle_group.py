
from particle import Particle


class ParticleManager:
    def __init__(self):
        self.particles: list[Particle] = []

    def electric_field_at_point(self, point: list[float]) -> list[float]:
        field_total = [0, 0]

        if len(self.particles) < 1: return field_total

        for particle_i in self.particles:
            field_i = particle_i.electric_field_at(point)
            field_total = [field_total[0] + field_i[0],
                           field_total[1] + field_i[1]]

        return point

    def add_particle(self, new_particle: Particle) -> None:
        self.particles.append(new_particle)
