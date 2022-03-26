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

Fields=EMFields(
    Efield=[0,0,0]
) #here I am including my definition of the electric and magnetic field from my fields class, and I have set my E field to have 0 value

orbitalPeriod=Fields.Period(particle)
print(orbitalPeriod) 
#Above I am printing the value of the orbital period which gives 4.378913894394501e-08 and I calculate it analytically to compare
#When I calculate it myself, I get the exact same value, therefore my period is being calculated correctly.

ListForValuesForX=[] #list containing my position values of the proton for the x axis
ListForValuesForY=[] #list containing my position values of the proton for the y axis
time=0
while time<orbitalPeriod:  
#here I have created a loop which runs as long as the orbital period during which it updates the acceleration, thus the position of the proton
    particle.update(10**(-10), Fields.Efield, Fields.Bfield, 0, 0)
    time+=10**(-10)
    ListForValuesForX.append(particle.position[0])
    ListForValuesForY.append(particle.position[1])

#below I print out a graph of my proton's movement undre the constant magnetic field with no electric field
#It should print out a full circle theoretically, which it does 

plt.xlabel("position in x-axis")
plt.ylabel("position in y-axis")
plt.plot(ListForValuesForX, ListForValuesForY)
plt.show()

"""Below I am checking that my cirle printed in the graph is a proper circle, by looking at the radii on X and Y axis to see it they are 
consistent. The print gives:
-5.207037402145237e-18 1.3938521178661169e-11
-6.9691510183471065e-12 6.9691040619900906e-12
6.969274090948786e-12"""
print(min(ListForValuesForX), max(ListForValuesForX)) 
print(min(ListForValuesForY), max(ListForValuesForY)) 
orbitalradius=Fields.Radius(particle)
print(orbitalradius)    
