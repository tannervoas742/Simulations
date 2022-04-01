from SpaceSim.Components.Component import _Component
from SpaceSim.Ammunition.KineticRound import KineticRound
from SpaceSim.BackEndSources.DataStructures import MathList, TypeCounter


class KineticCannon(_Component):
    def __init__(self, *Modules):
        _Component.__init__(self, *Modules)
        self.Name = 'Kinetic Cannon'
        self.Types += ['Kinetic', 'Weaponry']
        self.Define('Armor'         , 10  )            #3x
        self.Define('Endurance'     , 30  )            #1x
        self.Define('Shielding'     , None) #MathList  #1x
        self.Define('Energy'        , 5   )
        self.Define('Power'         , 10  )            #2x
        self.Define('Tick'          , 0   )
        self.Define('Tock'          , 1   )
        self.Define('Energy Storage', 20  )            #0.2x
        self.Define('Cargo Storage' , 0   )            #0.5x
        self.Define('Bandwidth'     , 10  )            #0.5x
        self.Define('Mass'          , 89  )
        self.Define('Thrust'        , 0   )            #1x
        self.Define('Ammunition'    , TypeCounter((KineticRound, 100)))

        self.Finish()