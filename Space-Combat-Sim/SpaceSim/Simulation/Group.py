import cupy as cp

class Group:
    GroupHash = {}
    def __init__(self, GroupID=[0]):
        self.ID = GroupID[0]
        GroupID[0] += 1
        Group.GroupHash[self.ID] = self

        self.Members = {}
        