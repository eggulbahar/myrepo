import numpy as np
import copy
import math
from pandas import Period
from particlegit import Particle

"""This is my new class which inherits from my previous particle class, which has defined variables as particle name,
velocity, mass, acceleration, position and the method through some of these are calculated. When inheriting these I have also included a
new attribute of my particle which is charge."""

class ChargedParticle(Particle):

#Below I have defined a function within my new class which initializes data attributes and a method for the charged particle, it takes 
# everything from the parent class of particle, through the useage of inheritance and adds a new attribute of charge
    def __init__(self, position=np.array( [0,0,0],dtype =float), velocity=np.array( [0,0,0],dtype =float), acceleration=np.array( [0, -10,0],dtype =float), name='Ball', mass=1.0, method="Euler-Richardson", charge=1.0):
        super().__init__(position=position, velocity=velocity, acceleration=acceleration, name=name, mass=mass, method=method)
        self.charge = charge #here I am defining the charge attribute which is an addition on top of my inheritance

#Below I have a special function which defines how to print the attributes of the charged particle
    def __str__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(
            self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)

#Below I have defined a function for my angular frequency, which will be a constant value, as the particle charge, mass and the magnetic
# field defined are constant 
    def angularfrequency(self, Bfield):
        return self.charge*np.linalg.norm(Bfield)/self.mass
         

 #Below I define the Lorentz force, which depends on the variables Efield= electric field and Bfield=magnetic field. I will define the 
 # fields on another page. However, when the particle is within certain limits is the only place where the electric field is not zero. 
 # This limit is defined in the y axis between a dafined distance of points -partRadius and partRadius. The reason it is named partRadius
 # is because I set the value later on to be a 0.05x of the initial Radius of the particle     
    def LorentzForce(self, Efield, Bfield, time, partRadius):
        Force=[0,0,0]
        if abs(self.position[1])<partRadius:
            Force=np.array(self.charge*Efield*math.cos(self.angularfrequency(Bfield)*time)+self.charge*np.cross(self.velocity,Bfield),dtype=float)#+self.charge*np.cross(self.velocity,Bfield)
        else:
            Force=self.charge*np.cross(self.velocity,Bfield)
        return Force

#I am going to connect my Lorentz force to the acceleration using the F=ma equation:
    def Updateacceleration(self, Efield, Bfield, time, partRadius):
        self.acceleration=self.LorentzForce(Efield, Bfield, time, partRadius)/self.mass
        
        
   #I have added the acceleration update below in my general update method, to make it simpler when using it later on in the simulation.
   # However, the above Updateacceleration method will stay as it is used by the Euler-Richardson method  
     
    def update(self, deltaT, Efield, Bfield, time, partRadius):
    #Here depending on the method that has been stated the correct method to calculate the velocity and position are assigned
    #Below I have taken the update function from my previous particle class and overrid it so it applies to the new current situation
        if np.linalg.norm(Efield)!=0 or np.linalg.norm(Bfield)!=0:
            self.acceleration=self.LorentzForce(Efield, Bfield, time, partRadius)/self.mass

        if self.method=="Euler":
            self.updateEuler(deltaT)
        elif self.method=="Euler-Cromer":
            
            self.updateECromer(deltaT)
        elif self.method=="Euler-Richardson":
            self.updateERichardson(deltaT, Efield, Bfield, time, partRadius)

    def updateERichardson (self, deltaT, Efield, Bfield, time, partRadius):
    #This method updates the velocity and position using the Euler-Richardson method. 
    #Below I have taken the method from particle class and overrided it.
        midself=copy.deepcopy(self)
        midvelocity=midself.velocity+midself.acceleration*0.5*deltaT #I have calculated the middle point veloicty and position
        midposition=midself.position+0.5*midself.velocity*deltaT
        midself.velocity=midvelocity
        midself.position=midposition
        if np.linalg.norm(Efield)!=0 or np.linalg.norm(Bfield)!=0:
            midself.Updateacceleration(Efield, Bfield, time+0.5*deltaT, partRadius)
        newvelocity=self.velocity+midself.acceleration*deltaT #using the middle values I have worked out the new position and velocity
        newposition=self.position+midself.velocity*deltaT
        self.velocity=newvelocity
        self.position=newposition  

    
        