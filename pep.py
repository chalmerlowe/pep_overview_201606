# <demo> silent
# Title: pep_demo1.py
# Usage: From an IPython prompt:
#        %run demobatch.py pep_demo1.py
# Description: Demoing and discussing a number of fun an interesting peps from the python programming language.
# Date: 20160628
# Revision: 0.5
# Python Version: 3.x
# IPython Version: 2.x
# Author: Chalmer Lowe

# TODO: N/A
# ============================================================================



# <demo> silent
#
# Matrix multiplication
# PEP 465

import numpy as np

a = np.ones((3, 3))
b = np.array([1, 2, 3, 1, 2, 3, 1, 2, 9]).reshape((3, 3))

c = a @ b
c



# <demo> silent
#
# Unpacking Generalizations
# PEP 448

# A common example of unpacking...
# limited to a single unpacking operation per function call

e = [1, 2, 3, 4, 5, 6]
print('hello', *e)

# hello 1 2 3 4 5 6

f = ('a', 'b', 'c')

print('hello', *e, 'world', *f)


# <demo> silent
#

t = *range(4), 4
t

# <demo> silent
#


u = [*range(4), 4]
u

# <demo> silent
#


v = {*range(4), 4, *(5, 6, 7)}
v

# <demo> silent
#

w = {'x': 1, **{'y': 2}, **{'z': 3}}
w


# <demo> silent
#
# Type hints
# PEP 484 and 483

def greeting(name: str) -> str:
    return 'Hello ' + name


# <demo> silent
#
# ZIPAPP
# PEP 441

# create an executable self-contained within in a zip archive 

# allows for ease of distribution, without requiring extraction, etc.



# <demo> silent
#
# os.scandir()
# PEP 471

# difference between os.walk(), os.listdir() and os.scandir()




# <demo> silent
#
# *.pyo file removal...

#... confusion about levels of optimization between
# *.pyc
# *.pyo     two separate levels of optimization...
# *.pyo


# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#




# <demo> silent
#





