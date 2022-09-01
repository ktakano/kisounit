# coding: utf-8
# Written by K. Takano

from activation import relu, sigmoid
import numpy as np

x1, x2 = 1.0, 0.8
w11, w12 = 0.5, 0.1
w21, w22 = 0.3, 0.2
b1, b2 = 0.1, 0.3

y1 = w11 * x1 + w12 * x2 + b1
y2 = w21 * x1 + w22 * x2 + b2

z1 = relu(y1)
z2 = relu(y2)

print(z1)
print(z2)

def _weight1(x1, x2):
    w11, w12 = 0.5, 0.1
    w21, w22 = 0.3, 0.2
    b1, b2 = 0.1, 0.3

    _y1 = w11 * x1 + w12 * x2 + b1
    _y2 = w21 * x1 + w22 * x2 + b2

    return _y1, _y2
 
def _activate1(_y1, _y2):
    y1 = relu(_y1)
    y2 = relu(_y2)

    return y1, y2

def layer1(x1, x2):
    _y1, _y2 = _weight1(x1, x2)
    y1, y2 = _activate1(_y1, _y2)

    return y1, y2

def _weight2(x1, x2):
    w11, w12 = 0.7, 0.8
    w21, w22 = 0.1, 0.4
    b1, b2 = 0.2, 0.4

    _y1 = w11 * x1 + w12 * x2 + b1
    _y2 = w21 * x1 + w22 * x2 + b2

    return _y1, _y2

def _activate2(_y1, _y2):
    y1 = sigmoid(_y1)
    y2 = sigmoid(_y2)

    return y1, y2

def layer2(x1, x2):
    _y1, _y2 = _weight2(x1, x2)
    y1, y2 = _activate2(_y1, _y2)

    return y1, y2

x = np.array([1.0, 0.8]) # 入力する値: x1, x2
output1 = np.array([0.0, 0.0]) # 1層目の出力値: y1, y2
output2 = np.array([0.0, 0.0]) # 2層目の出力値: y1, y2
output1[0], output1[1] = layer1(x[0], x[1])
output2[0], output2[1] = layer2(output1[0], output1[1])

print (output1)
print (output2)
