import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields
import pytest

"""Here I will use pytest to check that my particle has indeed been accelerated and has a final speed, which is mor than the initial speed"""
#Below I create my particle
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

#Below I am updating the speed of the proton inside the cyclotron and I record it in a list
times=[0]
speed=[np.linalg.norm(particle.velocity)] #list containing all the speed values for when the particle is inside the cyclotron
time=0

#The loop below updates the variables for the particle and records the speed values while the particle poasition is inside the cyclotron radius
while np.linalg.norm(particle.position)<Cyclotronradius:
    particle.update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
    time+=5e-12
    times.append(time)
    speed.append(np.linalg.norm(particle.velocity))

#Below I use pytest to check that the initial speed is always less than the final one, and that my particle has been accelerated
def test_velocity():
    assert speed[0]<speed[len(speed)-1]