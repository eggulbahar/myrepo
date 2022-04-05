# myrepo
There are 4 classes that the simulation uses in total, which are the files: particlegit, chargedparticlegit, EMField, Protons.

"particlegit" is the file with my original Particle class created for PHYS281 project, which contains velocity and acceleration update methods for Euler, Euler-Cromer, and Euler Richardson. The class can update kinetic energy, momentum, angular momentum, and contains other methods, which will not be needed for this project.

"chargedparticlegit" is the field with the ChargedParticle class, which inherits from Particle and introduces a new attribute of charge to the particle/object. This class can update angular frequency, which is used to update Lorentz force. The update function and Updateacceleration functions are changed for this class, where it becomes in terms of Lorentz force. Should be noted that the Lorentz force calculates an oscillating electric field (which oscillates for every half period) for certain y-position limits named partRadius.

"EMField" is the file with the EMFields class, which defines the electric and magnetic field, giving them initial values. The Lorentz force method from the ChargedParticle class will need to use this class' attributes to be able to update position, velocity and etc. The class contains methods defining orbital radius and period of the particle motion.

"Protons" is the file containing the MultipleProtons class. The class generates multiple protons, with randomized initial y-position (which still is within the limits of the slit). The class has methods calculating the mean speed, mean kinetic energy, and the mean and the standard deviation of the absolute values of the position of the protons.

Suggested order to look at the files:

"TestingWithoutEfield" is the file where I set the electric field to be 0 and only have a constant magnetic field in z-direction, and update the particle for 1 orbital period. A position graph is printed for a single proton showing that it does a full complete circle.

"testing protons class" is a file that uses the MultipleProtons class to produce a position distribution graph for multiple protons and also produces a graph of average fractional speed change while completing an orbit. SHould be noted that still there is no electric field and there is only a constant magnetic field.

"Kinetic energy graph for multiple protons" file produces the fractional change in kinetic energy for multiple protons, when there is not electric field applied and ther is only a constant magnetic field applied.

"VaryingElectricFieldForSingleProton" file is the full cyclotron simulation for a single proton. It has a varying electric field and constant magnetic field. Produces a position graph of the proton as it moves inside and outside the cyclotron.

"KE_velocity_anmomentum graphs for proton" file produces graphs of kinetic energy, speed, angular momentum magnitude as a function of time for a single proton inside a cyclotron with oscillating electric field and constant magnetic field. 

"MultipleProtonsInCyclotron" file produces a position graph of several protons with randomized initial y-positions using the MultipleProtons class.

My pytests:
There are 4 in total pytests. "runpytest" is the main file, which runs them all at once.

"test_chargedparticlegit" tests if ChargedParticle correctly inherits from Particle by checking y-velocity value.

"test_methods" starts by comparing the three numerical methods used in particle without using pytest. It considers a case of no electric field and just constant magnetic field. Produces position, position vector magnitude, speed, kinetic energy, momentum magnitude, and angular momentum magnitude graphs for all the numerical methods. This shows that Euler-Richardson is the more accurate than the others, as the rest would not conserve energy and momentum. The pytest checks to ensure that in the end Euler-Richardson is the method that has diverged the least out of all.

"test_velocitycomparison" checks that the final particle speed is always greater than the initial one for the case of a working cyclotron, using pytest.

"test_KE" check that every time my proton passes the gap with the electric field, it always gains the same amount of kinetic energy. Does that by having two lists, one for KE values before the particle enters the gap and one for after it exits it. the pytest takes the difference between the lists and checks that they are always the same value.