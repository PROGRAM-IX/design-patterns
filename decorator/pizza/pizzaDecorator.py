from pizza import Pizza

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.p = pizza

    def cost(self):
        return self.p.cost()
        
