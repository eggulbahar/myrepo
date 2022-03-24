import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields

"""This is the page where I will test the period of a particle's motion, in this case that of a single proton. I will set my electric field 
to be 0 and I will have a constant magnetic field in hte z-axis only."""

#below I have defined my particle which is a single proton, with given initial velocity in the x axis
protonmass=1.6726219*10**(-27)
protoncharge=1.6*10**(-19)
particle=ChargedParticle(
    position=np.array( [0,0,0],dtype =float),
    velocity=np.array( [0,1e-3,0],dtype =float),
    acceleration=np.array( [0,0,0],dtype =float),
    name='proton', 
    mass=protonmass,  
    charge=protoncharge
)

Fields=EMFields() #here I am including my definitionf of the electric and magnetic field from my fields class

orbitalPeriod=Fields.Period(particle)
print(orbitalPeriod) 
#Above I am printing the value of the orbital period which gives 6.568370841591752e-08 and I calculate it analytically to compare
#When I calculate it myself, I get the exact same value, therefore my period is being calculated correctly.

ListForValuesForX=[] #list containing my position values of the proton for the x axis
ListForValuesForY=[] #list containing my position values of the proton for the y axis
time=0
while time<orbitalPeriod:  
#here I have created a loop which runs as long as the orbital period during which it updates the acceleration, thus the position of the proton
    particle.Updateacceleration(Fields.Efield, Fields.Bfield)
    particle.update(10**(-5), Fields.Efield, Fields.Bfield)
    time+=10**(-5)
    ListForValuesForX.append(particle.position[0])
    ListForValuesForY.append(particle.position[1])

#below I print out a graph of my proton's movement undre the constant magnetic field with no electric field
#It should print out a full circle theoretically, which it does 

plt.plot(ListForValuesForX, ListForValuesForY)
plt.show()

"""Below I am checking that my cirle printed in the graph is a proper circle, by looking at the radii on X and Y axis to see it they are 
consistent. The print gives:
-2.0907773745432283e-06 2.090777374949499e-06
-4.1815547497971884e-06 -8.124185580930228e-16
2.0907773750014236e-06"""
print(min(ListForValuesForX), max(ListForValuesForX)) 
print(min(ListForValuesForY), max(ListForValuesForY)) 
orbitalradius=Fields.Radius(particle)
print(orbitalradius)    
