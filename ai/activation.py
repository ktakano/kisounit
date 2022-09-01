# coding: utf-8
# Written by K. Takano

import numpy as np

def step(x):
    if x > 0:
        y = 1
    else:
        y = 0
    
    return y

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

def relu(x):
    if x > 0:
        y = x
    else:
        y = 0
    
    return y
