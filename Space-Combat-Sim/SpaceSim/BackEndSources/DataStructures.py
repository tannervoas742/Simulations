import cupy as cp

class MathList:
    def __init__(self, *Args):
        self.Data = list(Args)

    def __add__(self, Other):
        Args = []
        for Index in range(len(self.Data)):
            Args += [self.Data[Index] + Other.Data[Index]]
        New = MathList()
        New.Data = Args
        return New

    def __sub__(self, Other):
        Args = []
        for Index in range(len(self.Data)):
            Args += [self.Data[Index] - Other.Data[Index]]
        New = MathList()
        New.Data = Args
        return New

    def __mul__(self, Other):
        Args = []
        for Index in range(len(self.Data)):
            Args += [self.Data[Index] * Other.Data[Index]]
        New = MathList()
        New.Data = Args
        return New

    def __div__(self, Other):
        Args = []
        for Index in range(len(self.Data)):
            Args += [self.Data[Index] / Other.Data[Index]]
        New = MathList()
        New.Data = Args
        return New

    def __repr__(self):
        return ', '.join(list(map(lambda Item: str(Item), self.Data)))

class TypeCounter:
    def __init__(self, *args):
        self.Data = {}
        for Item in args:
            self.Data[Item[0]] = Item[1]

    def __repr__(self):
        Keys = list(sorted(list(self.Data.keys()), key=lambda Key: self.Data[Key]))
        Data = []
        for Key in Keys:
            Name = Key().Name
            Data += ['{} X {}'.format(self.Data[Key], Name)]
        return ', '.join(Data)

    def __iter__(self):
        return self.Data.__iter__()

    def __getitem__(self, Key):
        return self.Data[Key]
