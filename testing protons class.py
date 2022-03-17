from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics
from EMField import EMFields

groupofprotons=MultipleProtons(numberofparticles=100)
Fields=EMFields()
print(groupofprotons)
print(groupofprotons.particles[0], groupofprotons.particles[1])


#trying to plot a distribution graph for position
positionvalues=[]
for i in range(groupofprotons.numberofparticles):
    positionvalues.append(np.linalg.norm(groupofprotons.particles[i].position))

sortednumbers=sorted(positionvalues)

mean = statistics.mean(sortednumbers)
sd = statistics.stdev(sortednumbers)

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
"""After plotting my graphs I notice that the the average particle position is at the middle"""

ListForValuesFor=[] #list containing my position values of the protons
time=0
while time<1:
    for i in range(groupofprotons.numberofparticles):
        groupofprotons.particles[i].Updateacceleration(Fields.Efield, Fields.Bfield)
        groupofprotons.particles[i].update(10**(-5), Fields.Efield, Fields.Bfield)
        ListForValuesFor.append(np.linalg.norm(groupofprotons.particles[i].position))
    time+=10**(-5)

sortedlistforvalues=sorted(ListForValuesFor)
mean2 = statistics.mean(sortedlistforvalues)
sd2 = statistics.stdev(sortedlistforvalues)
print(mean2)
print(mean)
plt.ylabel("Fraction of total particles")
plt.xlabel("Magnitude of the position vector")
plt.plot(sortedlistforvalues, norm.pdf(sortedlistforvalues, mean2, sd2), label="after some time")
plt.plot(sortednumbers, norm.pdf(sortednumbers, mean, sd), label="original")   
plt.legend()
plt.show()
        