import numpy as np
import copy
import math
from chargedparticlegit import ChargedParticle

"""Here I will create a class that has my fields, and checks the period and calculates the orbit of the particle. It takes defiitions of 
variables from the charged particle class."""

class EMFields(ChargedParticle):
    def __init__(
    self,
    Bfield=np.array([0,0,5], dtype=float),
    Efield=np.array([0,0,0], dtype=float)
    ):
        self.Bfield=np.array(Bfield, dtype=float)
        self.Efield=np.array(Efield, dtype=float)
    
        

