import numpy as np
from chargedparticlegit import ChargedParticle
import random 
from scipy.stats import norm
import statistics

"""Here I have created a class which defines multiple particles for the simulation. It generates particles with rnadom y-position, which
will be in the boundary of the slit. This class furthermore can calculate the varibles needed for a distribution function of the randomized
 initial positions of the protons (such as mean, and standard deviation), mean kinetic energy and mean speed."""

class MultipleProtons(ChargedParticle):
    def __init__(self, position=np.array( [0,0,0],dtype =float), velocity=np.array( [0,0,0],dtype =float), acceleration=np.array
    ( [0, -10,0],dtype =float), name='proton', protonmass=1.6726219*10**(-27), method="Euler-Richardson", protoncharge=1.6*10**(-19), numberofparticles=5):
        super().__init__(position=position, velocity=velocity, acceleration=acceleration, name=name, mass=protonmass, method=method, charge=protoncharge)
        self.numberofparticles=numberofparticles
        self.particles=[]
        for purticle in range(self.numberofparticles):
            newparticle=self.newparticle(purticle)
            self.particles.append(newparticle)
    
    #The initial/begining speeds of the protons should be non-relativistic therefore I chose it to be 10^(-3) m/s
    #Below I define every new particle to have a random position between the limit of my slit which I define to be between -10^(-4) to 10^(-4)
    def newparticle(self, number):
        self.velocity=np.array( [0, 1e-3,0], dtype=float  ) 
        
        self.position=np.array([0,random.uniform(-10**(-4),10**(-4)), 0])
        randomparticle = ChargedParticle(
            position=self.position,
            velocity=self.velocity,
            mass=self.mass,
            charge=self.charge,
            name=self.name+str(number)
        )
        return randomparticle


    def __str__(self):
        return 'This is a group of {0} protons with random positions.'.format(self.numberofparticles)


#Below I have added a method calculating the mean and the standard deviation of the absolute values of the position of the protons
    def distributioncalculation(self):
        valuesposition=[]
        for i in range(self.numberofparticles):
            valuesposition.append(self.particles[i].position[1])
        sortednumbers=sorted(valuesposition)
        meanp = statistics.mean(sortednumbers)
        sdp = statistics.stdev(sortednumbers)
        return [meanp, sdp, sortednumbers]

#Below is the mean kinetic energy calculation of the particles
    def meanKE(self):
            KE=0. 
            for i in range(self.numberofparticles):
                KE+=self.particles[i].kineticEnergy()
            KE/=self.numberofparticles
            return KE

#Below is a method calculating the average speed of the particles
    def meanSpeed(self):
        Speed= 0.
        for i in range(self.numberofparticles):
            Speed += np.linalg.norm(self.particles[i].velocity)
            
        Speed/=self.numberofparticles
        return Speed