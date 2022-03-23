from Protons import MultipleProtons
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
import statistics
from EMField import EMFields

groupofprotons=MultipleProtons(numberofparticles=5)
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
#plt.show()

#I have transferred the methodolgy of calculating mean and standard deviation, which I tested here, to the particle class
"""After plotting my graphs I notice that the the average particle position is at the middle"""

ListForValuesFor=[] #list containing my position values of the protons
time=0

counter=0


timeSeries = [0.,]
speedSeries = [groupofprotons.meanSpeed(),]


while time<1:
    
    for i in range(groupofprotons.numberofparticles):
        
        groupofprotons.particles[i].update(1e-5, Fields.Efield, Fields.Bfield)
        
    time+=10**(-5)
    counter+=1 
    if (counter%1000==0): 
        print(time,groupofprotons.meanKE(),groupofprotons.meanSpeed())
        timeSeries.append(time)
        speedSeries.append(groupofprotons.meanSpeed())


x = np.array(timeSeries, dtype=float)
y = np.array(speedSeries, dtype=float)

DeltaY = (y-speedSeries[0])/speedSeries[0]

plt.plot(x,DeltaY)
plt.ylabel("Fractional Change in Average Speed")
plt.xlabel("Time (s)")

plt.show()

