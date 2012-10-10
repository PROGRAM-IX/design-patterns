from ice_cream import ice_cream

class ice_cream_decorator(ice_cream):
    def __init__(self, i):
        self.i = i

    def cost(self):
        return self.i.cost()
