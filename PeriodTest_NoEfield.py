import numpy as np
import math
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields
import pytest as py

"""This is the page where I will test the period of a particle's motion, in this case that of a single proton. I will set my electric field 
to be 0 and I will have a constant magnetic field in hte z-axis only."""

protonmass=1.6726219*10**(-27)
protoncharge=1.6*10**(-19)
particle=ChargedParticle(
    position=np.array( [0,0,0],dtype =float),
    velocity=np.array( [200,0,0],dtype =float),
    acceleration=np.array( [0,0,0],dtype =float),
    name='proton', 
    mass=protonmass,  
    charge=protoncharge
)

Fields=EMFields()
orbitalPeriod=Fields.Period(particle)
print(orbitalPeriod) 
#Above I am printing the value of the orbital period which gives 6.568370841591752e-08 and I calculate it analytically to compare
#When I calculate it myself, I get the exact same value, however this is not my official test

ListForValuesForX=[]
ListForValuesForY=[]
time=0
while time<orbitalPeriod:
    particle.Updateacceleration(Fields.Efield, Fields.Bfield)
    particle.update(10**(-12), [])
    time+=10**(-12)
    ListForValuesForX.append(particle.position[0])
    ListForValuesForY.append(particle.position[1])

plt.ylim(-10**(-5),10**(-5))
plt.xlim(-10**(-5),10**(-5))
plt.plot(ListForValuesForX, ListForValuesForY)
plt.show()

    


