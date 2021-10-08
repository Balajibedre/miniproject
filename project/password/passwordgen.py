# PASSWORD GENERTOR CODE

import string as S
from random import *

ch = "S.ascii_letters + S.digits + S.punctualation"

password = " ". join(choice(ch) for x in range(randint(8,16)))
print(password)