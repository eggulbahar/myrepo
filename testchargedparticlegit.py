import numpy as np
import copy
from chargedparticlegit import ChargedParticle
import pytest

TestChargedParticleLilBoi=ChargedParticle(
    name="proton"
)

TestChargedParticleLilBoi.update(10,[])

print(TestChargedParticleLilBoi)