from arabica_factory import arabica_factory
from french_roast_factory import french_roast_factory

class coffee_shop():
    def test(self):
        a_f = arabica_factory()
        fr_f = french_roast_factory()
        for i in ["strong", "mild", "STRONG", "MILD"]:
            a_c = a_f.create_coffee(i)
            a_c.prepare()
            a_c.brew()
            a_c.fill_cup()
            fr_c = fr_f.create_coffee(i)
            fr_c.prepare()
            fr_c.brew()
            fr_c.fill_cup()
        a_cap = a_f.create_sachet_cappucino()
        a_cap.add_powder()
        a_cap.add_water()
        fr_cap = fr_f.create_sachet_cappucino()
        fr_cap.add_powder()
        fr_cap.add_water()

def main():
    c_s = coffee_shop()
    c_s.test()

if __name__ == "__main__":
    main()
