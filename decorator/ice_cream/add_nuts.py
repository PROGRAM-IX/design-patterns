from ice_cream_decorator import ice_cream_decorator

class add_nuts(ice_cream_decorator):
    def __init__(self, i):
        ice_cream_decorator.__init__(self, i)

    def cost(self):
        print "Nuts!"
        return self.i.cost() + 0.75
