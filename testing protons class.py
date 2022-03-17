from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics

groupofprotons=MultipleProtons(numberofparticles=100)
print(groupofprotons)
print(groupofprotons.particles[0], groupofprotons.particles[1])


#trying to plot a distribution graph for position
positionvalues=[]
for i in range(groupofprotons.numberofparticles):
    positionvalues.append(np.linalg.norm(groupofprotons.particles[i].position))

sortednumbers=sorted(positionvalues)

mean = statistics.mean(sortednumbers)
sd = statistics.stdev(sortednumbers)
plt.ylabel("Fraction of total particles")
plt.xlabel("Magnitude of the position vector")
plt.plot(sortednumbers, norm.pdf(sortednumbers, mean, sd))
plt.show()


#below I am plotting a distribution graph for the velocity
velocityvalues=[]
for i in range(groupofprotons.numberofparticles):
    velocityvalues.append(np.linalg.norm(groupofprotons.particles[i].velocity))

sortednumbersvelocity=sorted(velocityvalues)

mean1 = statistics.mean(sortednumbersvelocity)
sd1 = statistics.stdev(sortednumbersvelocity)
plt.ylabel("Fraction of total particles")
plt.xlabel("Magnitude of the velocity vector")
plt.plot(sortednumbersvelocity, norm.pdf(sortednumbersvelocity, mean1, sd1))
plt.show()

#I have transferred the methodolgy of calculating mean and standard deviation, which I tested here, to the particle class