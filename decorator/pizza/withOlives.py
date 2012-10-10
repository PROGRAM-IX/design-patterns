from pizzaDecorator import PizzaDecorator

class WithOlives(PizzaDecorator):
    def __init__(self, p):
        PizzaDecorator.__init__(self, p)
    
    def cost(self):
        print "Olives!"
        return self.p.cost() + 2
