import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields
from Protons import MultipleProtons

"""Here I am creating the simulation of the multiple protons (in this case 3) with randomized initial positions inside a cyclotron, with constant magnetic field
and a varying electric field."""

groupofprotons=MultipleProtons(numberofparticles=3)
Fields=EMFields()

Cyclotronradius=0.11
partRadius=1e-4

positionvaluesX=[[],[],[]]
positionvaluesY=[[],[],[]]

#The loop below updates the x and y positions of the protons under the presence of the electro-magnetic field. The inner while and if else
# loops assure that the particle is accelerating and experiences the fields only inside the cyclotron radius boundary. When outside of it the proton
# reaches constant speed and continues its path in a straigth line.
for i in range(groupofprotons.numberofparticles):
    time=0
    while np.linalg.norm(groupofprotons.particles[i].position)<1.5*Cyclotronradius:
        if np.linalg.norm(groupofprotons.particles[i].position)<Cyclotronradius:
            groupofprotons.particles[i].update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
            time+=5e-12
            positionvaluesX[i].append(groupofprotons.particles[i].position[0])
            positionvaluesY[i].append(groupofprotons.particles[i].position[1])
            
        else:
            groupofprotons.particles[i].acceleration=np.array([0,0,0], dtype=float)
            groupofprotons.particles[i].update(5e-12, [0,0,0], [0,0,0], time, 0)
            time+=5e-12
            positionvaluesX[i].append(groupofprotons.particles[i].position[0])
            positionvaluesY[i].append(groupofprotons.particles[i].position[1])
            

plt.xlabel("position in x-axis")
plt.ylabel("position in y-axis")

plt.plot(positionvaluesX[0], positionvaluesY[0], label="proton 1")
plt.plot(positionvaluesX[1], positionvaluesY[1], label="proton 2")
plt.plot(positionvaluesX[2], positionvaluesY[2], label="proton 3")
plt.legend()
plt.show()