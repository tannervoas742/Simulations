import SpaceSim
import SpaceSim.Ammunition as Ammunition
import SpaceSim.Components as Components
import SpaceSim.Entities as Entities
import SpaceSim.Simulation as Simulation
from SpaceSim.BackEndSources.Utils import FPrint

TestGroup1 = Simulation.Group()
FPrint(TestGroup1)

ENT1 = Entities.LightFighter()
FPrint(ENT1)