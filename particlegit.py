
"""this is my original class code from PHYS281, which describes a particle, its position, velocity, acceleration, mass, and name.
It is capable of updating its acceleration, velocity and position using various numerical methods."""
import numpy as np
import copy
class Particle:
    def __init__(
    #these are the inputs to my class with default values
    self,
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, -10, 0], dtype=float),
    name='Ball',
    mass=1.0,
    method="Euler-Richardson" 
    ):
    #I am assigning all inputs as data attributes 
        self.position=np.array(position, dtype=float)
        self.velocity=np.array(velocity, dtype=float)
        self.acceleration=np.array(acceleration, dtype=float)
        self.name=name
        self.mass=mass
        self.G=6.67408e-11
        self.method=method

    def updateGravitationalAcceleration(self, celestialbodies):
        finalacceleration=0
        for body in celestialbodies:    
            #In this loop I have found the gravitational acceleration that the object experiences due to multiple bodies and added them all together
            displacement=-body.position+self.position
            distance=np.sqrt(displacement[0]**2+displacement[1]**2+displacement[2]**2)
            finalacceleration+=-self.G*body.mass*(distance**-3)*displacement
        self.acceleration=finalacceleration

    def update(self, deltaT, celestialbodies):
    #Here depending on the method that has been stated the correct method to calculate the velocity and position are assigned
        if self.method=="Euler":
            self.updateEuler(deltaT)
        elif self.method=="Euler-Cromer":
            
            self.updateECromer(deltaT)
        elif self.method=="Euler-Richardson":
            self.updateERichardson(deltaT, celestialbodies)   

    def updateEuler(self, deltaT):
    #This method updates the velocity and position using the Euler method
        newposition=self.position+self.velocity*deltaT
        newvelocity=self.velocity+self.acceleration*deltaT
        self.position=newposition
        self.velocity=newvelocity

    def updateECromer(self, deltaT):
    #This method updates the velocity and position using the Euler-Cromer method
        newvelocity=self.velocity+self.acceleration*deltaT
        newposition=self.position+newvelocity*deltaT
        self.position=newposition
        self.velocity=newvelocity
       

    def updateERichardson (self, deltaT, celestialbodies):
    #This method updates the velocity and position using the Euler-Richardson method. 
        midself=copy.deepcopy(self)
        midcelestialbodies=copy.deepcopy(celestialbodies)
        midvelocity=midself.velocity+midself.acceleration*0.5*deltaT #I have calculated the middle point veloicty and position
        midposition=midself.position+0.5*midself.velocity*deltaT
        midself.velocity=midvelocity
        midself.position=midposition
        for midbody in midcelestialbodies:
            midvelocity=midbody.velocity+midbody.acceleration*0.5*deltaT
            midposition=midbody.position+0.5*midbody.velocity*deltaT
            midbody.velocity=midvelocity
            midbody.position=midposition
        midacceleration=0 #I am calculating the middle acceleration using my values for the middle bodies
        for midbody in midcelestialbodies:
            middisplacement=-midbody.position+midself.position
            middistance=np.sqrt(middisplacement[0]**2+middisplacement[1]**2+middisplacement[2]**2)
            midacceleration+=-midself.G*midbody.mass*(middistance**-3)*middisplacement
        midself.acceleration=midacceleration
        newvelocity=self.velocity+midself.acceleration*deltaT #using the middle values I have worked out the new position and velocity
        newposition=self.position+midself.velocity*deltaT
        self.velocity=newvelocity
        self.position=newposition

    def kineticEnergy(self):
    #Here I have created a method to calculate the kinetic energy of an object
        kineticEnergy=self.mass*0.5*np.linalg.norm(self.velocity)**2
        return kineticEnergy

    def potentialEnergy(self, celestialbodies):
    #Here I have created a method to calculate the potential energy of an object, using a list of other bodies
        potentialEnergy=0
        for body in celestialbodies:
            potentialEnergy+=self.mass*np.dot((self.position-body.position), self.acceleration)
        return potentialEnergy

    def momentum(self):
    #Here I have created a method to calculate the linear momentum of an object
        momentum=self.mass*self.velocity
        return momentum

    def angularmomentum(self):
    #Here I have created a method to calculate the angular momentum of an object, using the equation for momentum crossed with position
        linearmomentum = self.momentum()
        angularmomentum=np.cross(np.array(linearmomentum,dtype=float),np.array(self.position,dtype=float))
        return angularmomentum
        
    def __str__(self):
    #I have defined how my object is printed
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
        )