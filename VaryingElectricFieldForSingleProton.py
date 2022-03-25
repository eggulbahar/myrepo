import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields

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

Fields=EMFields()

orbitalPeriod=Fields.Period(particle)
orbitalRadius=Fields.Radius(particle)
partRadius=0.05*orbitalRadius
print(orbitalRadius)
print(partRadius)
print(orbitalPeriod)


x=[]
y=[]
ts=[0]
kes=[particle.kineticEnergy()]
time=0
counter=0
while time<5*orbitalPeriod:
    time+=10**(-3)
    particle.update(10**(-3), Fields.Efield, Fields.Bfield, time, partRadius)
    ts.append(time)
    kes.append(particle.kineticEnergy())
    counter+=1
    if (counter%10==0): 
        x.append(particle.position[0])
        y.append(particle.position[1])
        
orbitalPeriod=Fields.Period(particle)
orbitalRadius=Fields.Radius(particle)
partRadius=orbitalRadius
print(orbitalRadius)
print(partRadius)
print(orbitalPeriod)
print(kes[0],kes[1])
plt.plot(x, y)
plt.show()

plt.plot(ts,kes)
plt.show()