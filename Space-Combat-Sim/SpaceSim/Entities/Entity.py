import cupy as cp

class _Entity:
    EntityHash = {}
    def __init__(self, EntityID=[0]):
        self.Group = None
        self.ID = EntityID[0]
        EntityID[0] += 1
        self.Components = []

    def Add(self, Component):
        self.Components.append(Component)

    #def __repr__(self):
