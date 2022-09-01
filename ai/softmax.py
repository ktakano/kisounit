import numpy as np

# coding: utf-8
# Written by K. Takano

def softmax(x):
    exp = np.exp(x - np.max(x)) # np.max(x): 補正項 (オーバーフロー対策)
    sum_exp = np.sum(exp)

    output = exp / sum_exp
    
    return output