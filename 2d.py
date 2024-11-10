import matplotlib.pyplot as plt
numpy as np
fig, ax = plt.subplots(figsize=(8, 8))
ax. set_aspect ('equal','box')
ax set_facecolor ("black")
ax.grid(color="white", linestyle="—-", linewidth=0.5, alpha=0.3)

sun_radius = 0.1
planet_sizes= [0.03, 0.05, 0.06, 0.07, 0.09, 0.07, 0.06, 0.051]
orbit_radii = [10.3,0.5,0.7, 0.9, 1.2, 1.5,1.8, 2.11]
colors = l'orange', 'gray', 'yellow', 'red', 'brown', 'orange', 'blue', 'cyan'] # Planet colors
sun = plt. Circle((0, 0), sun_radius, color=‘yellow')

ax. add_patch (sun)
for radius, size, color in zip(orbit_radii, planet_sizes, colors):
orbit = plt.Circle((0, 0), radius, color='white', linestyle='--', fill=False)
ax.add_patch(orbit)

angle = np. random. rand () * 2 * np.pi
x, y = radius * np. cos (angle), radius* np.sin(angle)
planet = plt. Circle((x, y), size, color=color)
ax-add_patch(planet)

ax.set_xlim(-2.5,2.5)
ax.set_ylim(-2.5,2.5)
ax axis( 'on') 

plt. title("2DSolar System Visualization with Grid")
plt. show ()
