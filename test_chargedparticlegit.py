import numpy as np
from chargedparticlegit import ChargedParticle
import pytest
"""this is a test to check that my inheritance (the inital one) is working, that it takes the methods from the original 
file and prints calculations"""


def test_answer():
    assert TestChargedParticle.velocity[1]==-100.
    """assert TestChargedParticle.velocity[0]==1. This is an example tried to make pytest fail."""

TestChargedParticle=ChargedParticle(
    name="proton",
    method="Euler-Cromer" 
    )

TestChargedParticle.update(10,[0,0,0], [0,0,0], 0, 0)

print(TestChargedParticle)
print(TestChargedParticle.velocity)

"""I ran the test which calculated not lorentz force but the origical acceleration and velocity due to gravity as I have not changed gravity
with lorentz force in my inheritance yet. So far I have tested if my simple inheritence is working and I got the result of:
Particle: proton, Mass: 1.000e+00, Position: [    0. -1000.     0.], Velocity: [   0. -100.    0.], Acceleration: [  0. -10.   0.]   
in my terminal, which is as expected showing that my inheritance is working, indicating that I can move onto more complex code writing"""

"""Now I will try to do this test by using pytest, to learn the package better so I can use it later on more complex code testing.
I added a function named above as "test_answer" which tests the y and x velocity values. I intentionally gave the x velocity
a wrong to see how pytest functioned. Now that I am confident that my inheritence is working and I know how to use pytest I will move
onto changing my forces and starting my main modelling."""