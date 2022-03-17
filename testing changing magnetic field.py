from EMField import EMFields
from Protons import MultipleProtons
import random 
from matplotlib import pyplot as plt
from scipy.stats import norm
import statistics


fields=EMFields(Bfield=[0,0,100]) #the magnetic field in the negative x axis
fields2=EMFields(Bfield=[0,0,110]) #here I have a 10% step increase for the magnetic field in positive x axis (half of my cyclotron)
protons=MultipleProtons(velocity=[0,random.uniform(0,100),0], numberofparticles=100)

plt.ylabel("Fraction of total particles")
plt.xlabel("Magnitude of the position vector")
plt.plot(protons.meancalculation()[4], norm.pdf(protons.meancalculation()[4], protons.meancalculation()[0], protons.meancalculation()[1]))
plt.show()
