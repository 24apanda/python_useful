# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:26:27 2017

@author: apanda88
"""
#####example.py is the module created which will be called
import example
import imp  ########use for reload
p=example.add(12,13)
imp.reload(example)

print(p)

import sys
sys.path
print(sys.path)

print(dir(example))#########names insidethe module

print(imp.__doc__)