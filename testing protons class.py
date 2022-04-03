from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics
from EMField import EMFields

"""Here I am testing some of the characteristics of my multiple protons class. I start by doing a position probability distribution graph,
 as all the particles start with an intial random y-position. Next I plot the fractional change in mean speed value, to confirm that for the
 case of 0 electric field and constant magnetic field. The fractional change should be zero as there is no external work put into the 
 system and the particle is not being accelerated."""

groupofprotons=MultipleProtons(numberofparticles=5)
Fields=EMFields(
    Bfield=[0,0,10**(-8)], 
    Efield=[0,0,0]  #setting the electric field to be
)
"""print(groupofprotons)
print(groupofprotons.particles[0], groupofprotons.particles[1])"""

#trying to plot a distribution graph for position:
#I use the method defined in the multiple protons class

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
        timeSeries.append(time)
        speedSeries.append(groupofprotons.meanSpeed())

x = np.array(timeSeries, dtype=float)
y = np.array(speedSeries, dtype=float)

DeltaY = (y-speedSeries[0])/speedSeries[0]  #calculating the fractional change in the mean speed

plt.plot(x,DeltaY)
plt.ylabel("Fractional Change in Average Speed")
plt.xlabel("Time (s)")

plt.show()

