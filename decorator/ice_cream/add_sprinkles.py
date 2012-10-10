from ice_cream_decorator import ice_cream_decorator

class add_sprinkles(ice_cream_decorator):
    def __init__(self, i):
        ice_cream_decorator.__init__(self, i)    
        
    def cost(self):    
        print "Sprinkles!"
        return self.i.cost() + 0.4

