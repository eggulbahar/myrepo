import numpy as np
import math

"""Here I have created a class that has my electromagnetic fields, and checks the period and calculates the orbit of the particle. It takes
 definitions of variables from the charged particle class."""

class EMFields():
    #Below I am identifying the inputs to my class, which are the magnetic and electric field
    # There is an initial constant magnetic field value given in the z-direction only
    #There is also an initial value for the electric field in the y-axis, this will become the amplitude value for it, as the Lorentz force
    # function from the ChargedParticle class will make the value oscillate. 
    def __init__(
    self,
    Bfield=np.array([0,0,1.5], dtype=float),
    Efield=np.array([0,50000/2e-4,0], dtype=float) 
    ):
        self.Bfield=np.array(Bfield, dtype=float)
        self.Efield=np.array(Efield, dtype=float)


    #Below is defined a method calculating the period of the orbit that the particle does due to the constant magnetic field.
    #This value will be constant as all the varibales it depends on are too.
    def Period(self, chargedparticle):
        return (2*math.pi*chargedparticle.mass)/(chargedparticle.charge*np.linalg.norm(self.Bfield))   


    #Below I have defined the radius of the orbit the particle does. This will be an increasing value as the particle gains velocity, therefore
    #it will be updating.
    def Radius(self, chargedparticle):
        return (chargedparticle.mass*np.linalg.norm(chargedparticle.velocity))/(chargedparticle.charge*np.linalg.norm(self.Bfield))

