import math
import matplotlib.pyplot as plt

# sigmax = 80
# sigmay = 60
# touxy =  20

sigmax = float(input('Enter the value of horizontal normal stresses (N/m^2) (tensile positive): '))
sigmay = float(input('Enter the value of vertical normal stresses (N/m^2) (tensile positive): '))
touxy =  float(input('Enter the value of shear stresses (N/m^2) (clockwise positive): '))

xface = [sigmax, -touxy]
yface = [sigmay, touxy]

r = math.sqrt(math.pow((xface[0] - xface[1]), 2) + math.pow((yface[0] - yface[1]), 2)) / 2

theta = [i * math.pi / 180 for i in range(360)]

centerx = (sigmax + sigmay) / 2

x = [centerx + r * math.cos(theta[i]) for i in range(len(theta))]
y = [r * math.sin(theta[i]) for i in range(len(theta))]

plt.plot(x, y)
plt.axis('equal')
plt.grid(True)
plt.show()
