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


x=[particle.position[0]]
y=[particle.position[1]]
time=0
counter=0
while np.linalg.norm(particle.position)<1.5*Cyclotronradius:
    if np.linalg.norm(particle.position)<Cyclotronradius:
        particle.update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
        time+=5e-12
        x.append(particle.position[0])
        y.append(particle.position[1])
    else:
        particle.update(5e-12, [0,0,0], [0,0,0], time, 0)
        time+=5e-12
        x.append(particle.position[0])
        y.append(particle.position[1])
        

plt.xlabel("position in x-axis")
plt.ylabel("position in y-axis")
plt.plot(x, y)
plt.show()

