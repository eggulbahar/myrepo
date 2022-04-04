import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields

"""This page produces graphs of velocity, kinetic energy and angular momentum as a function of time for a proton inside a cyclotron"""

#Below I have defined my particle as a proton
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

Cyclotronradius=0.11 #This is a similar value to the original experiment values
partRadius=1e-4 #this is going to be the limit of the gap, which is again taken to be a similar value from that of the original experiment

#Below the kinetic energy, speed and angular mometum values are being updated for when the particle is within the limits of the cyclotron
times=[0]
KEvalues=[particle.kineticEnergy()]
speed=[np.linalg.norm(particle.velocity)]
angmomentum=[np.linalg.norm(particle.angularmomentum())]
time=0
while np.linalg.norm(particle.position)<Cyclotronradius:
    particle.update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
    time+=5e-12
    times.append(time)
    KEvalues.append(particle.kineticEnergy())
    speed.append(np.linalg.norm(particle.velocity))
    angmomentum.append(np.linalg.norm(particle.angularmomentum()))

#This will print the final velocity in terms of c
print(speed[len(speed)-1]/(2.9979*10**(8)))

#Below are my plotting functions:
plt.xlabel("Time (s)")
plt.ylabel("Kinetic energy (eV)")
plt.plot(times,KEvalues)
plt.show()

plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.plot(times, speed)
plt.show()

plt.xlabel("Time (s)")
plt.ylabel("Angular Momentum (Js)")
plt.plot(times, angmomentum)
plt.show()