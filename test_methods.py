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
    position=np.array( [-0.6e-11,0,0],dtype =float),
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
        positions[j].append((abs(np.linalg.norm(data[j][i].position))))
        velocities[j].append((abs(np.linalg.norm(data[j][i].velocity))))
        energies[j].append((abs(data[j][i].kineticEnergy())))
        momentums[j].append((abs(np.linalg.norm(data[j][i].momentum()))))
        angularmomentums[j].append((abs(np.linalg.norm(data[j][i].angularmomentum()))))

for i,method in enumerate(methods):
    plt.plot(xs[i],ys[i],label=method)
plt.xlabel('position in x-axis (m)')
plt.ylabel('position in y-axis (m)')
plt.legend()
plt.show()

for i,method in enumerate(methods):
    plt.plot(times[1:len(times)],positions[i],label=method)
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


def test_method():
    # 219 timesteps in simulated orbits
    assert positions[2][218]<=positions[1][218] and positions[2][218]<=positions[0][218]
    assert velocities[2][218]<=velocities[1][218] and velocities[2][218]<=velocities[0][218]
    assert energies[2][218]<=energies[1][218] and energies[2][218]<=energies[0][218]
    assert momentums[2][218]<=momentums[1][218] and momentums[2][218]<=momentums[0][218]
    assert angularmomentums[2][218]<=angularmomentums[1][218] and angularmomentums[2][218]<=angularmomentums[0][218]

retcode = pytest.main()