import cupy as cp
import SpaceSim.BackEndSources.Utils as Utils
from SpaceSim.Ammunition.Ammunition import _Ammunition

class KineticRound(_Ammunition):
    def __init__(self):
        _Ammunition.__init__(self)
        self.Name = 'Kinetic Round'
        self.Behaviors = []
        self.Mass = 1