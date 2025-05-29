# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from particle_group import ParticleManager
from particle import Particle

def draw(particles, limits, h=0.1):

    # Defining plot
    fig, ax1 = plt.subplots()

    # Creating arrows
    x = np.arange(limits[0], limits[1], h)
    y = np.arange(limits[0], limits[1], h)
    X, Y = np.meshgrid(x, y)

    x_function = np.vectorize(particles.electric_field_x)
    y_function = np.vectorize(particles.electric_field_y)

    # u, v = electric_vector_function(X, Y)

    u = x_function(X, Y)
    v = y_function(X, Y)
    #u = np.cos(X)*Y
    #v = np.sin(y)*Y

    n = -2

    # Defining color
    color = np.sqrt(((v-n)/2)*2 + ((u-n)/2)*2)

    # Creating plot
    ax1.quiver(X, Y, u, v, color, alpha=0.8)
    ax1.xaxis.set_ticks([])
    ax1.yaxis.set_ticks([])
    ax1.axis([limits[0] - 0.2, limits[1] + 0.1, limits[0] - 0.2, limits[1] + 0.1])
    ax1.set_aspect('equal')
    ax1.set_title('electric field')

    # Draw Particles:
    for particle in particles.particles:
        color = 'r' if particle.charge > 0 else 'b'
        ax1.add_patch(plt.Circle((particle.pos[0], particle.pos[1]), 0.05, color=color))

    # show figure
    plt.tight_layout()
    plt.show()


def main():
    particles = ParticleManager()

    particles.add_particle(Particle(0, 1, 1.602e-19))
    particles.add_particle(Particle(0, -1, -1.602e-19))

    draw(particles, [-2, 2], h=0.125)


if __name__ == "__main__":
    main()
