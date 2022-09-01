# coding: utf-8
# Written by K. Takano

# 入力が1つの場合の例
x = 1.0
w = 0.5
b = 0.1

_y = w * x + b

# 入力が2つの場合の例
x1, x2 = 1.0, 0.8
w1, w2 = 0.5, 0.1
b = 0.1

_y = w1 * x1 + w2 * x2 + b

# 2入力の関数を定義
def  _two_input(x1, x2, w1, w2, b):
    _y = w1 * x1 + w2 * x2 + b

    return _y

# _two_input()関数を使用して、
# w1 = 0.5、w2 = 0.5、b = 0.7 として、
# (x1, x2) = (0.0, 0.0)、(1.0, 0.0)、(0.0, 1.0)、(1.0, 1.0)
# の出力を確認する。

w1, w2 = 0.5, 0.5
b = -0.7

x1, x2 = 0.0, 0.0
_y = _two_input(x1, x2, w1, w2, b)
print(_y)

x1, x2 = 1.0, 0.0
_y = _two_input(x1, x2, w1, w2, b)
print(_y)

x1, x2 = 0.0, 1.0
_y = _two_input(x1, x2, w1, w2, b)
print(_y)

x1, x2 = 1.0, 1.0
_y = _two_input(x1, x2, w1, w2, b)
print(_y)

def _and_weight(x1, x2):
    w1, w2 = 0.5, 0.5
    b = -0.7

    _y = _two_input(x1, x2, w1, w2, b)

    return _y

def _and_activate(_y):
    if _and_weight (x1, x2) <= 0:
        y = 0
    else:
        y = 1

    return y

def AND(x1, x2):
    _y = _and_weight(x1, x2) # 重み付け
    y = _and_activate(_y) # 活性化
    
    return y

# AND()関数を使用して、
# (x1, x2) = (0.0, 0.0)、(1.0, 0.0)、(0.0, 1.0)、(1.0, 1.0)
# の出力を確認

x1, x2 = 0.0, 0.0
y = AND(x1, x2)
print(y)

x1, x2 = 1.0, 0.0
y = AND(x1, x2)
print(y)

x1, x2 = 0.0, 1.0
y = AND(x1, x2)
print(y)

x1, x2 = 1.0, 1.0
y = AND(x1, x2)
print(y)