import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields

protonmass=1.6726219*10**(-27)
protoncharge=1.6*10**(-19)
particle=ChargedParticle(
    position=np.array([0,0,0],dtype =float),
    velocity=np.array([0,1e-3,0],dtype =float),
    acceleration=np.array([0,0,0],dtype =float),
    name='proton', 
    mass=protonmass,  
    charge=protoncharge
)

Fields=EMFields()

orbitalPeriod=Fields.Period(particle)
orbitalRadius=Fields.Radius(particle)
Cyclotronradius=0.11
partRadius=1e-4
"""print(orbitalRadius)
print(partRadius)
print(orbitalPeriod)"""


x=[particle.position[0]]
y=[particle.position[1]]
times=[0]
KEvalues=[particle.kineticEnergy()]
time=0
counter=0
while np.linalg.norm(particle.position)<1.5*Cyclotronradius:
    if np.linalg.norm(particle.position)<Cyclotronradius:
        particle.update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
        time+=5e-12
        times.append(time)
        KEvalues.append(particle.kineticEnergy())
        x.append(particle.position[0])
        y.append(particle.position[1])
    else:
        particle.update(5e-12, [0,0,0], [0,0,0], time, 0)
        time+=5e-12
        times.append(time)
        KEvalues.append(particle.kineticEnergy())
        x.append(particle.position[0])
        y.append(particle.position[1])
        
"""orbitalPeriod=Fields.Period(particle)
orbitalRadius=Fields.Radius(particle)
partRadius=orbitalRadius
print(orbitalRadius)
print(partRadius)
print(orbitalPeriod)
print(kes[0],kes[1])"""
plt.xlabel("position in x-axis")
plt.ylabel("position in y-axis")
plt.plot(x, y)
plt.show()

plt.xlabel("Time (s)")
plt.ylabel("Kinetic energy (eV)")
plt.plot(times,KEvalues)
plt.show()