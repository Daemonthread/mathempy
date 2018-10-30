import sys
import time
sys.path.append("../src")
from mathempy import Mathempy

mhp = Mathempy(headless=True)

print(mhp.basket_list())
print(mhp.basket_total())

mhp.basket_add_item(url="https://www.mathem.se/varor/fusilli/pasta-fusilli-500g-barilla", quantity=5)
mhp.basket_add_item(url="https://www.mathem.se/varor/smacitrus/clementiner-klass1", quantity=20)
mhp.basket_add_item(url="https://www.mathem.se/varor/blockljus/blockljus-stearin-6x9cm", quantity=1)

print(mhp.basket_list())
print(mhp.basket_total())

mhp.exit()