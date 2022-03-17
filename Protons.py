import numpy as np
from chargedparticlegit import ChargedParticle
import random 
from scipy.stats import norm
import statistics

class MultipleProtons(ChargedParticle):
    def __init__(self, position=np.array( [0,0,0],dtype =float), velocity=np.array( [0,0,0],dtype =float), acceleration=np.array
    ( [0, -10,0],dtype =float), name='proton', protonmass=1.6726219*10**(-27), method="Euler-Cromer", protoncharge=1.6*10**(-19), numberofparticles=5):
        super().__init__(position=position, velocity=velocity, acceleration=acceleration, name=name, mass=protonmass, method=method, charge=protoncharge)
        self.numberofparticles=numberofparticles
        self.particles=[]
        for purticle in range(self.numberofparticles):
            newparticle=self.newparticle(purticle)
            self.particles.append(newparticle)
    
    #the initial/begining speeds of the protons should be non-relativistic therefore I chose the range to be from 0 to 100 m/s
    def newparticle(self, number):
        self.velocity=np.array([random.uniform(-10**(-8),10**(-8)), random.uniform(-10**(-8),10**(-8)), 0])
        self.position=np.array([random.uniform(-1,1), random.uniform(-1,1), 0])
        randomparticle = ChargedParticle(
            position=self.position,
            velocity=self.velocity,
            mass=self.mass,
            charge=self.charge,
            name=self.name+str(number)
        )
        return randomparticle

    def __str__(self):
        return 'This is a group of {0} protons with random positions and velocities.'.format(self.numberofparticles)

#below I have added a method calculating the mean and the standard deviation of the absolute values of the velocity and position of the protons
    def meancalculation(self):
        valuesposition=[]
        valuesvelocity=[]
        for i in range(self.numberofparticles):
            valuesposition.append(np.linalg.norm(self.particles[i].position))
            valuesvelocity.append(np.linalg.norm(self.particles[i].velocity))
        sortednumbers=sorted(valuesposition)
        sortednumbersvelocity=sorted(valuesvelocity)
        meanp = statistics.mean(sortednumbers)
        sdp = statistics.stdev(sortednumbers)
        meanv=statistics.mean(sortednumbersvelocity)
        sdv=statistics.stdev(sortednumbersvelocity)
        return [meanp, sdp, meanv, sdv, sortednumbers, sortednumbersvelocity]

