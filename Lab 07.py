import matplotlib.pyplot as plt
import numpy as np

# Data
x = 0.01
y = 0.01
z = 0.001

A_x = y * z
A_z = x * y

E = 8.3 * 10**10

d_xz = 110 * 10**(-12)
d_zz = 370 * 10**(-12)

e_0 = 8.85418781762039 * 10**(-12)
e_r = 1200

F = np.array([10**0, 10**1, 10**2, 10**3, 10**4, 10**5])

# Thickness
t = 1000 * (z + ((-1) * F * z) / (E * A_z)) 

fig1 = plt.figure()

plt.scatter(F, t, c='k')

plt.xlabel('Force (N)')
plt.xscale('log')

plt.ylabel('Thickness (mm)')

plt.savefig('thickness.png', dpi = 300)

# Voltage
V_x = (F * x * d_xz) / (e_0 * e_r * A_x)
V_z = (F * z * d_zz) / (e_0 * e_r * A_z)

fig2 = plt.figure()

data1 = plt.scatter(F, V_x)
data2 = plt.scatter(F, V_z)

plt.legend((data1, data2), ('V_x', 'V_z'))

plt.xlabel('Force (N)')
plt.xscale('log')

plt.ylabel('Voltage (V)')
plt.yscale('log')
plt.ylim(10**(-1), 3 * 10**6)

plt.savefig('voltage.png', dpi = 300)