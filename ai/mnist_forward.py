# coding: utf-8
# Written by K. Takano
import sys, os
import numpy as np
import pickle
from mnist import load_mnist
from activation import sigmoid
from softmax import softmax

(x_train, t_train), (x_test, t_test) = load_mnist()
x_train = x_train.astype(np.float32)
x_train /= 255.0

with open("mnist_weight.pkl", 'rb') as f:
    weight = pickle.load(f)

W1, W2, W3 = weight['W1'], weight['W2'], weight['W3']
b1, b2, b3 = weight['b1'], weight['b2'], weight['b3']

mnist_image = x_train[0] # 推定用のmnist画像
correct_num = t_train[0] # 正解の数

# 1層目
_y1 = np.dot(mnist_image, W1) + b1
y1 = sigmoid(_y1)

# 2層目
_y2 = np.dot(y1, W2) + b2
y2 = sigmoid(_y2)

# 3層目
_y3 = np.dot(y2, W3) + b3
y3 = softmax(_y3)

predict_num = np.argmax(y3) # 最大値となるインデックスを取得

print("推定: ", predict_num)
print("正解: ", correct_num)
