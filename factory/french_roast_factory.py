from drinks_factory import drinks_factory
from strong_french import strong_french
from mild_french import mild_french
from french_roast_sachet import french_roast_sachet

class french_roast_factory(drinks_factory):
    def create_coffee(self, strength):
        if strength.lower() == "strong":
            return strong_french()
        elif strength.lower() == "mild":
            return mild_french()

    def create_sachet_cappucino(self):
        return french_roast_sachet()
