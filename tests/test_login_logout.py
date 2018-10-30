import sys
import getpass
sys.path.append("../src")
from mathempy import Mathempy

try:
    username = sys.argv[1]
except IndexError as e:
    print("please provide a username: 'python test_login_logout.py test@example.com'")
    exit(1)
password = getpass.getpass()

mhp = Mathempy(headless=True)
returned = mhp.login(username, password)
if not returned:
    print("Login Failed.")
print("Login Success")

mhp.logout()
mhp.exit()