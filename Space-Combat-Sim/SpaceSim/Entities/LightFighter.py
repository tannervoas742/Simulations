from SpaceSim.Entities.Entity import _Entity
from SpaceSim.Components.KineticCannon import KineticCannon

class LightFighter(_Entity):
    def __init__(self):
        _Entity.__init__(self)
        self.Name = "Light Fighter"

        self.Add(KineticCannon())