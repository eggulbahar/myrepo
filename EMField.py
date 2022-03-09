import numpy as np
import math

"""Here I will create a class that has my fields, and checks the period and calculates the orbit of the particle. It takes defiitions of 
variables from the charged particle class."""

class EMFields():
    #below I am identifying the inputs to my class, which are the magnetic and electric field
    def __init__(
    self,
    Bfield=np.array([0,0,1], dtype=float),
    Efield=np.array([0,0,0], dtype=float)
    ):
        self.Bfield=np.array(Bfield, dtype=float)
        self.Efield=np.array(Efield, dtype=float)

    def Period(self, chargedparticle):
        return (2*math.pi*chargedparticle.mass)/(chargedparticle.charge*self.Bfield[2])   

    def Radius(self, chargedparticle):
        return (chargedparticle.mass*chargedparticle.velocity)/(chargedparticle.charge*self.Bfield[2])

