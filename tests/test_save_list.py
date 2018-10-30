import sys
import getpass
sys.path.append("../src")
from mathempy import Mathempy

try:
    username = sys.argv[1]
    basket_name = sys.argv[2]
except IndexError as e:
    print("please provide a username and basket name: 'python test_login_logout.py test@example.com basket_test42'")
    exit(1)

password = getpass.getpass()

mhp = Mathempy(headless=True)
logged_in = mhp.login(username, password)
if not logged_in:
    print("Login Failed.")
else:
    print("Login Success")

mhp.clear_basket()

print("Before: --------------------------")
print("Basket contents: {}".format(mhp.basket_list()))
print("Basket total: {}kr".format(mhp.basket_total()))

mhp.basket_add_item(url="https://www.mathem.se/varor/fusilli/pasta-fusilli-500g-barilla", quantity=5)
mhp.basket_add_item(url="https://www.mathem.se/varor/smacitrus/clementiner-klass1", quantity=20)
mhp.basket_add_item(url="https://www.mathem.se/varor/blockljus/blockljus-stearin-6x9cm", quantity=1)

print("After: --------------------------")
print("Basket contents: {}".format(mhp.basket_list()))
print("Basket total: {}kr".format(mhp.basket_total()))

print("Saving basket as {}".format(basket_name))
saved = mhp.save_basket(basket_name)

if not saved:
    print("Basket not saved.")
else:
    print("Basket Saved.")

mhp.logout()
mhp.exit()