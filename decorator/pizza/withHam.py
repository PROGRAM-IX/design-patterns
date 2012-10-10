from pizzaDecorator import PizzaDecorator

class WithHam(PizzaDecorator):
    def __init__(self, p):
        PizzaDecorator.__init__(self, p)
    
    def cost(self):
        print "Ham!"
        return self.p.cost() + 3

