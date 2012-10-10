from withHam import WithHam
from withOlives import WithOlives
from smallPizza import SmallPizza
from largePizza import LargePizza

p = SmallPizza()
p_o_h = WithHam(WithOlives(SmallPizza()))
print p.cost()
print ""
print p_o_h.cost()
