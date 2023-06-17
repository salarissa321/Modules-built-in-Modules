

#----------------------------------------
#------- Modules => Built in Modules----
#-----------------------------------------
# [1] Module Is A File Contain A Set Of Functions
# [2] You can import Module In Your App To Help You
# [3] You can import Multiple Modules
# [4] You can Create Your Own Modules
# [5] Modules Saves Your Ti,e
#-----------------------------------------

# import main Module


import random
# print(random)
print(f"Print Random Float Number {random.random()}") # Print Random Float Number 0.6474878695422105

print("#" * 50) # ##################################################


# Show All Function Inside Modules 


import random
print(dir(random)) 
['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print("#" * 50) # ##################################################

# import One or Two Functions From Module

from random import randint
print(f"Print Rand Integer {randint(100,900)} ")

# Print Rand Integer 295
# Print Rand Integer 456
# Print Rand Integer 808

print("#" * 50) # ##################################################

# import One or Two Functions From Module

from random import randint , random
print(f"Print Random float {random()} ") # Print Random float 0.8932062059306782
print(f"Print Rand Integer {randint(100,900)} ") # Print Rand Integer 343
