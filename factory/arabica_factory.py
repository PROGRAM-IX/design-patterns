from drinks_factory import drinks_factory
from strong_arabica import strong_arabica
from mild_arabica import mild_arabica
from arabica_sachet import arabica_sachet

class arabica_factory(drinks_factory):
    def create_coffee(self, strength):
        if strength.lower() == "strong":
            return strong_arabica()
        elif strength.lower() == "mild":
            return mild_arabica()
    
    def create_sachet_cappucino(self):
        return arabica_sachet()
