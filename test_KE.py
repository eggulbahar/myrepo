import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields

"""Here I am doing a pytest to check that every time my proton passes the gap it always gains the same amount of kinetic energy."""

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

#Below I define my field using the EMFields class created before:
Fields=EMFields()

#Defining orbital period:
Period=Fields.Period(particle)

#Values for cyclotron dimensions and slit separation:
Cyclotronradius=0.11 
partRadius=1e-4

times=[]
KEvaluesbefore=[] #Kinetic energy before the particle enters the gap
KEvaluesafter=[] #Kinetic energy after the particle leaves the gap
time=0
indexes=list(range(0,101))

#The loop below updates the methods with time and records kinetic energies in the lists above
#The KE values recorded are those that are before and after the particle passes through the slit
while np.linalg.norm(particle.position)<Cyclotronradius:
    particle.update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
    time+=5e-12
    times.append(time)
    for i in indexes:
        if time==((i*Period)+Period/4): #This is every quarter of a period, which corresponds to before entering the slit
            KEvaluesbefore.append(particle.kineticEnergy())
        if time==((i*Period)+3*Period/4): #3/4 of the Period corresponds to KE value for after leaving the slit
            KEvaluesafter.append(particle.kineticEnergy())

#Below is my pytest, which checks that the kinetic energy gained every time should be the same amount, it checks that the differences between
#  KE before it enters the gap and after it exits it, is always the same
def test_KineticEnergy():
    for index in range(len(KEvaluesbefore)-1):
        assert KEvaluesafter[index]-KEvaluesbefore[index]==KEvaluesafter[index+1]-KEvaluesbefore[index+1]