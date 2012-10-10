from ice_cream_decorator import ice_cream_decorator
from vanilla import vanilla
from strawberry import strawberry
from add_nuts import add_nuts
from add_honey import add_honey
from add_sprinkles import add_sprinkles

v_nh = add_honey(add_nuts(vanilla()))
s_hs = add_sprinkles(add_honey(strawberry()))
v_nhs = add_sprinkles(add_honey(add_nuts(vanilla())))

for i in [v_nh, s_hs, v_nhs]:
    print i.cost()
