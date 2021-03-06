from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from EMField import EMFields

"""This file produces a fractional change in kinetic energy graph over time for multiple protons with randomized initial positions, when 
there's no electric field present and there's only a constant magnetic field."""

groupofprotons=MultipleProtons(numberofparticles=5)
Fields=EMFields(
    Bfield=[0,0,10**(-8)],
    Efield=[0,0,0]
)

#To calculate the fractional change in kinetic energy for the multiple protons, the code initially calculates the mean kinetic energy using
#the method from the MultipleProtons class

time=0
counter=0
timeSeries = [0.,]
KEseries = [groupofprotons.meanKE(),]

while time<1:    
    for i in range(groupofprotons.numberofparticles):
        
        groupofprotons.particles[i].update(10**(-3), Fields.Efield, Fields.Bfield, 0, 1)
        
    time+=10**(-3)
    counter+=1  #The counter makes the run time of the code shorter, only recording data in certain steps.
    if (counter%100==0): 
        timeSeries.append(time)
        KEseries.append(groupofprotons.meanKE())


x = np.array(timeSeries, dtype=float)
y = np.array(KEseries, dtype=float)

#Below the fractional change is calculated
DeltaY = (y-KEseries[0])/KEseries[0] 

plt.plot(x,DeltaY)
plt.ylabel("Fractional Change in Average Kinetic Energy")
plt.xlabel("Time (s)")

plt.show()

"""When I plot the graph I observe that the fractional deviation is almost 0, which is the value it should have as there's no currently apparent
electric field. To test conservation of energy and to make sure that it is conserved I am going to increase the time step the update
runs to see if with more presicion the fractional change will get larger. If that is the case than energy seems to be conserved in my
simulation.
Initial time step value= time+=10**(-5)
Test time step value= time+=10**(-3)
After running both graphs, I observe that indeed the fractional change value gets closer to 0 as the time step decreases, which 
increases the accuracy of the run."""