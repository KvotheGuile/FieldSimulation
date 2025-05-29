
from particle import Particle


class ParticleManager:
    def __init__(self):
        self.particles: list[Particle] = []

    def electric_field_at_point(self, point: list[float]) -> list[float]:

        return point

    def add_particle(self, new_particle: Particle) -> None:
        self.particles.append(new_particle)
