import cupy as cp
import SpaceSim.BackEndSources.Utils as Utils

class _Ammunition:
    def __init__(self):
        self.Name = 'NONE'
        self.Behaviors = []
        self.Mass = 0

    def __repr__(self):
        Table = {
            '1#Type': self.Name,
            '2#Mass': self.Mass
        }
        return Utils.TableToText(Table)