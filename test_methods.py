import numpy as np
from matplotlib import pyplot as plt
from chargedparticlegit import ChargedParticle
from EMField import EMFields
import pytest
import copy
methods=['Euler','Euler-Cromer','Euler-Richardson']
data=[[],[],[]]
times=[]
fields=EMFields(
    Efield=[0,0,0]
)
protonmass=1.6726219*10**(-27)
protoncharge=1.6*10**(-19)
generalproton=ChargedParticle(
    position=np.array( [0,1e-11,0],dtype =float),
    velocity=np.array( [0,1e-3,0],dtype =float),
    acceleration=np.array( [0,0,0],dtype =float),
    name='proton', 
    mass=protonmass,  
    charge=protoncharge,
)
for index,currentmethod in enumerate(methods):
    proton=copy.deepcopy(generalproton)
    proton.method=currentmethod
    orbitalPeriod=fields.Period(proton)
    time=0
    data[index].append(proton)
    if currentmethod=='Euler':
        times.append(time)
    while time<5*orbitalPeriod:
        proton.update(10e-10,fields.Efield,fields.Bfield,0,0)
        time+=10e-10
        data[index].append(copy.deepcopy(proton))
        if currentmethod=='Euler':    #
            times.append(time)

'''
filename='testdata.npy'
np.save(filename,data,allow_pickle=True)
'''
xs=[[],[],[]]
ys=[[],[],[]]
positions=[[],[],[]]
velocities=[[],[],[]]
energies=[[],[],[]]
momentums=[[],[],[]]
angularmomentums=[[],[],[]]
for j in range(len(methods)):
    for i in range(1,len(times)):
        xs[j].append(data[j][i].position[0])
        ys[j].append(data[j][i].position[1])
        positions[j].append((np.linalg.norm(data[j][i].position)-np.linalg.norm(data[j][0].position))/(np.linalg.norm(data[j][0].position)))
        velocities[j].append((np.linalg.norm(data[j][i].velocity)-np.linalg.norm(data[j][0].velocity))/(np.linalg.norm(data[j][0].velocity)))
        energies[j].append((data[j][i].kineticEnergy()-data[j][0].kineticEnergy())/(data[j][0].kineticEnergy()))
        momentums[j].append((np.linalg.norm(data[j][i].momentum())-np.linalg.norm(data[j][0].momentum()))/(np.linalg.norm(data[j][0].momentum())))
        angularmomentums[j].append((np.linalg.norm(data[j][i].angularmomentum())-np.linalg.norm(data[j][0].angularmomentum()))/(np.linalg.norm(data[j][0].angularmomentum())))

plt.plot(xs[0],ys[0])
plt.plot(xs[1],ys[1])
plt.plot(xs[2],ys[2])
plt.xlabel('position in x-axis')
plt.ylabel('position in y-axis')
plt.show()