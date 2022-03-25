import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields
from Protons import MultipleProtons


groupofprotons=MultipleProtons(numberofparticles=2)
Fields=EMFields()
"""print(groupofprotons)
print(groupofprotons.particles[0], groupofprotons.particles[1])"""

Cyclotronradius=0.11
partRadius=1e-4

counter=0

positionvaluesX=[[],[]]
positionvaluesY=[[],[]]


for i in range(groupofprotons.numberofparticles):
    time=0
    while np.linalg.norm(groupofprotons.particles[i].position)<1.5*Cyclotronradius:
        if np.linalg.norm(groupofprotons.particles[i].position)<Cyclotronradius:
            groupofprotons.particles[i].update(5e-12, Fields.Efield, Fields.Bfield, time, partRadius)
            time+=5e-12
            positionvaluesX[i].append(groupofprotons.particles[i].position[0])
            positionvaluesY[i].append(groupofprotons.particles[i].position[1])
            
        else:
            groupofprotons.particles[i].update(5e-12, [0,0,0], [0,0,0], time, 0)
            time+=5e-12
            positionvaluesX[i].append(groupofprotons.particles[i].position[0])
            positionvaluesY[i].append(groupofprotons.particles[i].position[1])
            

plt.xlabel("position in x-axis")
plt.ylabel("position in y-axis")

plt.plot(positionvaluesX[0], positionvaluesY[0], label="proton 1")
plt.plot(positionvaluesX[1], positionvaluesY[1], label="proton 2")
plt.legend()
plt.show()