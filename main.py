# Import libraries
import numpy as np
import matplotlib.pyplot as plt

def draw(particles, limits, h=0.1):

    # Defining subplots
    fig, ax1 = plt.subplots(1, 1)

    # first subplot
    # Creating arrows
    x = np.arange(limits[0], limits[1], h)
    y = np.arange(limits[0], limits[1], h)
    X, Y = np.meshgrid(x, y)
    u = np.cos(X)*Y
    v = np.sin(y)*Y
    n = -2

    # Defining color
    color = np.sqrt(((v-n)/2)*2 + ((u-n)/2)*2)

    # Creating plot
    ax1.quiver(X, Y, u, v, color, alpha=0.8)
    ax1.xaxis.set_ticks([])
    ax1.yaxis.set_ticks([])
    ax1.axis([limits[0] - 0.2, limits[1] + 0.1, limits[0] - 0.2, limits[1] + 0.1])
    ax1.set_aspect('equal')
    ax1.set_title('meshgrid function')

    # show figure
    plt.tight_layout()
    plt.show()

def main():

    draw(None, [0, 2], h=0.1)

if __name__ == "__main__":
    main()
