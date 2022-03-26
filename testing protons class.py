from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics
from EMField import EMFields

groupofprotons=MultipleProtons(numberofparticles=5)
Fields=EMFields(
    Bfield=[0,0,10**(-8)],
    Efield=[0,0,0]
)
"""print(groupofprotons)
print(groupofprotons.particles[0], groupofprotons.particles[1])"""

#trying to plot a distribution graph for position:

values=groupofprotons.distributioncalculation()
plt.xlabel("Start position in y-axis")
plt.ylabel("Probability density function evaluated at x")
plt.plot(values[2], norm.pdf(values[2], values[0], values[1]))   
plt.show()
#After plotting my graphs I notice that the the average particle position is at the middle


#fractional change in average speed:
time=0
counter=0
timeSeries = [0.,]
speedSeries = [groupofprotons.meanSpeed(),]

while time<1:
    for i in range(groupofprotons.numberofparticles):
        groupofprotons.particles[i].update(1e-3, Fields.Efield, Fields.Bfield, 0, 1)
        
    time+=10**(-3)
    counter+=1 
    if (counter%10==0): 
        """print(time, groupofprotons.meanSpeed())"""
        timeSeries.append(time)
        speedSeries.append(groupofprotons.meanSpeed())

x = np.array(timeSeries, dtype=float)
y = np.array(speedSeries, dtype=float)

DeltaY = (y-speedSeries[0])/speedSeries[0]

plt.plot(x,DeltaY)
plt.ylabel("Fractional Change in Average Speed")
plt.xlabel("Time (s)")

plt.show()

