import cupy as cp
from SpaceSim.BackEndSources.DataStructures import MathList, TypeCounter
from SpaceSim.BackEndSources.Utils import TableToText

class _Component:
    def __init__(self, *Modules):
        self.Name = 'NONE'
        self.Types = []
        self.Stats = {}
        self.Define('Armor', 0)
        self.Define('Endurance', 0)
        self.Define('Shielding', MathList(0, 0))
        self.Define('Energy', 0)
        self.Define('Power', 0)
        self.Define('Tick', 0)
        self.Define('Tock', 0)
        self.Define('Energy Storage', 0)
        self.Define('Cargo Storage', 0)
        self.Define('Bandwidth', 0)
        self.Define('Mass', 0)
        self.Define('Thrust', 0)
        self.Define('Ammunition', TypeCounter())

        ModuleCounter = {}
        for Item in Modules:
            self = self + Item
            if Item.Name not in ModuleCounter:
                ModuleCounter[Item.Name] = 0
            ModuleCounter[Item.Name] += 1

        if len(Modules) > 0:
            self.Name = '{} ({})'.format(self.Name, ', '.join(list(map(lambda Key: '{}x{}'.format(ModuleCounter[Key], Key))))).replace('(, ', '(')

    def Define(self, Stat, Value=None):
        if Value != None:
            self.Stats[Stat] = Value

    def Finish(self):
        for Ammo in self.Stats['Ammunition']:
            self.Stats['Mass'] += Ammo().Mass * self.Stats['Ammunition'][Ammo]

    def __add__(self, Other):
        for Key in self.Stats:
            if type(self.Stats[Key]) == dict:
                for SubKey in Other.Stats[Key]:
                    if SubKey in self.Stats[Key]:
                        self.Stats[Key][SubKey] += Other.Stats[Key][SubKey]
                    else:
                        self.Stats[Key][SubKey] = Other.Stats[Key][SubKey]
            else:
                self.Stats[Key] = self.Stats[Key] + Other.Stats[Key]
        return self

    def __repr__(self):
        Output = ''
        Output += '{}\n'.format(self.Name)
        Output += TableToText(self.Stats) + '\n'
        for Ammo in self.Stats['Ammunition']:
            Output += str(Ammo()) + '\n'
        return Output.rstrip()
