# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Defining subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize =(14, 8))

# first subplot
# Creating arrows
x = np.arange(0, 2.2, 0.2)
y = np.arange(0, 2.2, 0.2)
X, Y = np.meshgrid(x, y)
u = np.cos(X)*Y
v = np.sin(y)*Y
n = -2

# Defining color
color = np.sqrt(((v-n)/2)*2 + ((u-n)/2)*2)

# Creating plot
ax1.quiver(X, Y, u, v, color, alpha = 0.8)
ax1.xaxis.set_ticks([])
ax1.yaxis.set_ticks([])
ax1.axis([-0.2, 2.3, -0.2, 2.3])
ax1.set_aspect('equal')
ax1.set_title('meshgrid function')

# second subplot
# Creating arrows
x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)
X, Y = np.meshgrid(x, y)
z = X * np.exp(-X**2 -Y**2)
dx, dy = np.gradient(z)
n = -2

# Defining color
color = np.sqrt(((dx-n)/2)*2 + ((dy-n)/2)*2)

# Creating plot
ax2.quiver(X, Y, dx, dy, color)
ax2.xaxis.set_ticks([])
ax2.yaxis.set_ticks([])
ax2.set_aspect('equal')
ax2.set_title('gradient')


# show figure
plt.tight_layout()
plt.show()



