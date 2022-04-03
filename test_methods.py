import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields
import pytest
import copy

"""Here I am conducting a pytest and comparing the accuracy of all the numerical methods that the code can use. This test is done for the case
when there is no electric field applied and there is only a constant magnetic field present. In this case the velocity and the kinetic energy of the
particle should always stay the same as there will not be any work done on the particle."""


#COMPARING THE METHODS
methods=['Euler','Euler-Cromer','Euler-Richardson']
data=[[],[],[]]
times=[]
fields=EMFields(
    Efield=[0,0,0]                        
)
protonmass=1.6726219*10**(-27)
protoncharge=1.6*10**(-19)
generalproton=ChargedParticle(
    position=np.array( [-0.6e-11,0,0],dtype =float),
    velocity=np.array( [0,1e-3,0],dtype =float),
    acceleration=np.array( [0,0,0],dtype =float),
    name='proton', 
    mass=protonmass,  
    charge=protoncharge,
)

#This loop runs 5 orbits for each numerical method and stores the time and copies of the proton into my main data array, where I can access
#all the information I need for my analysis such as velocity, kinetic energy, etc.
for index,currentmethod in enumerate(methods):
    proton=copy.deepcopy(generalproton) #proton copies for each method to use
    proton.method=currentmethod    
    orbitalPeriod=fields.Period(proton)
    time=0
    data[index].append(proton)   
    if currentmethod=='Euler': #the time is saved only once as it is the same for each method  
        times.append(time)
    while time<5*orbitalPeriod:
        proton.update(10e-10,fields.Efield,fields.Bfield,0,0) 
        time+=10e-10
        data[index].append(copy.deepcopy(proton))
        if currentmethod=='Euler':    
            times.append(time)


xs=[[],[],[]] #the data array for the x-position for each method
ys=[[],[],[]] #the data array for the y-position for each method
positions=[[],[],[]]  #magnitude of the position vector
velocities=[[],[],[]]   #speed, as it is the magnitude of the velocity
energies=[[],[],[]]   #kinetic energy
momentums=[[],[],[]]   #magnitude of momentum
angularmomentums=[[],[],[]]   #magnitude of angular momentum

#The loop below goes through each method and saves the information needed from the stored protons into their respective arrays
for j in range(len(methods)):
    for i in range(1,len(times)):   
        xs[j].append(data[j][i].position[0]) 
        ys[j].append(data[j][i].position[1])
        positions[j].append((abs(np.linalg.norm(data[j][i].position))))
        velocities[j].append((abs(np.linalg.norm(data[j][i].velocity))))
        energies[j].append((abs(data[j][i].kineticEnergy())))
        momentums[j].append((abs(np.linalg.norm(data[j][i].momentum()))))
        angularmomentums[j].append((abs(np.linalg.norm(data[j][i].angularmomentum()))))

for i,method in enumerate(methods):  #This loop plots a graph with results from each method
    plt.plot(xs[i],ys[i],label=method)
plt.xlabel('position in x-axis (m)')   
plt.ylabel('position in y-axis (m)')
plt.legend()
plt.show()

for i,method in enumerate(methods):
    plt.plot(times[1:len(times)],positions[i],label=method) #Here I use slicing, to avoid the first value, which is a zero and would cause overflow
plt.xlabel('Time')
plt.ylabel('position vector magnitude (m)')
plt.legend()
plt.show()

for i,method in enumerate(methods):
    plt.plot(times[1:len(times)],velocities[i],label=method)
plt.xlabel('Time')
plt.ylabel('velocity vector magnitude (m/s)')
plt.legend()
plt.show()

for i,method in enumerate(methods):
    plt.plot(times[1:len(times)],energies[i],label=method)
plt.xlabel('Time')
plt.ylabel('Kinetic energy (J)')
plt.legend()
plt.show()

for i,method in enumerate(methods):
    plt.plot(times[1:len(times)],momentums[i],label=method)
plt.xlabel('Time')
plt.ylabel('Momentum magnitude (kgm/s)')
plt.legend()
plt.show()

for i,method in enumerate(methods):
    plt.plot(times[1:len(times)],angularmomentums[i],label=method)
plt.xlabel('Time')
plt.ylabel('Angular momentum magnitude (kgm^2/s)')
plt.legend()
plt.show()


#BELOW IS MY PYTEST
#From my position graph I realize that Euler-Richardson is the most accurate, while the other methods diverge over time
#I therefore am testing that Richardson is better when it comes to conservation laws as well. 

def test_method():
    #I assert that at the final time-step where error is greatest Euler-Richardson will have diverged the least out of all the methods
    # 219 timesteps in simulated orbits
    assert positions[2][218]<=positions[1][218] and positions[2][218]<=positions[0][218]
    assert velocities[2][218]<=velocities[1][218] and velocities[2][218]<=velocities[0][218]
    assert energies[2][218]<=energies[1][218] and energies[2][218]<=energies[0][218]
    assert momentums[2][218]<=momentums[1][218] and momentums[2][218]<=momentums[0][218]
    assert angularmomentums[2][218]<=angularmomentums[1][218] and angularmomentums[2][218]<=angularmomentums[0][218]

