import numpy as np
import copy
import math
from particlegit import Particle

"""This is my new class which inherts from my previous particle class, which has defined variables as particle name,
velocity, mass, acceleration, position and the method through some of these are calculated. When inheriting these I have also included a
new attribute of my particle which is charge."""

class ChargedParticle(Particle):

#below I have defined a function within my new class which initializes data attributes and a method for the charged particle, it takes 
# everything from the parent class of particle, through the useage of inheritance and adds a new attribute of charge
    def __init__(self, position=np.array( [0,0,0],dtype =float), velocity=np.array( [0,0,0],dtype =float), acceleration=np.array( [0, -10,0],dtype =float), name='Ball', mass=1.0, method="Euler-Richardson", charge=1.0):
        super().__init__(position=position, velocity=velocity, acceleration=acceleration, name=name, mass=mass, method=method)
        self.charge = charge #here I am defining the charge attribute which is an addition on top of my inheritance

#below I have a special function which defines how to print the attributes of the charged particle
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(
            self.Name,self.mass,self.charge,self.position, self.velocity,self.acceleration)
 
 #below I define the Lorentz force, which depends on the variables Efield= electric field and Bfield=magnetic field. I will define the 
 # fields on another page   
    def LorentzForce(self, Efield, Bfield):
        return (self.charge*Efield+self.charge*np.cross(self.velocity, Bfield))

#Now I will create a test function to check my class, for this I will open a new file named: "test charged particle.py" 

#I am going to connect my Lorentz force to the acceleration using the F=ma equation:
    def Updateacceleration(self, Efield, Bfield):
        a=self.LorentzForce(Efield, Bfield)/self.mass
        return a