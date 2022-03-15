import numpy as np
from chargedparticlegit import ChargedParticle

class MultipleProtons(ChargedParticle):
    def __init__(self, position=np.array( [0,0,0],dtype =float), velocity=np.array( [0,0,0],dtype =float), acceleration=np.array
    ( [0, -10,0],dtype =float), name='proton', protonmass=1.6726219*10**(-27), method="Euler-Richardson", protoncharge=1.6*10**(-19), numberofparticles=1):
        super().__init__(position=position, velocity=velocity, acceleration=acceleration, name=name, mass=protonmass, method=method, charge=protoncharge)
        self.numberofparticles=numberofparticles




