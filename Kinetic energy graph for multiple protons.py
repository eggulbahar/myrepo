from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from EMField import EMFields

groupofprotons=MultipleProtons(numberofparticles=5)
Fields=EMFields()

time=0
counter=0
timeSeries = [0.,]
KEseries = [groupofprotons.meanKE(),]

while time<1:    
    for i in range(groupofprotons.numberofparticles):
        
        groupofprotons.particles[i].update(1e-5, Fields.Efield, Fields.Bfield)
        
    time+=10**(-5)
    counter+=1 
    if (counter%1000==0): 
        timeSeries.append(time)
        KEseries.append(groupofprotons.meanKE())

x = np.array(timeSeries, dtype=float)
y = np.array(KEseries, dtype=float)

DeltaY = (y-KEseries[0])/KEseries[0]

plt.plot(x,DeltaY)
plt.ylabel("Fractional Change in Average Kinetic Energy")
plt.xlabel("Time (s)")

plt.show()

