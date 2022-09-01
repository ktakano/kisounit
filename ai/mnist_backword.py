# coding: utf-8
# Written by K. Takano
import sys, os
import numpy as np
import pickle
from mnist import load_mnist, to_one_hot
from activation import sigmoid
from softmax import softmax

def get_sample_mnist ():
    (x_train, t_train), (x_test, t_test) = load_mnist()
    x_train = x_train.astype(np.float32)
    x_train /= 255.0

    mnist_image = x_train[0] # 推定用のmnist画像
    corrects = to_one_hot(t_train)
    correct = corrects[0]

    mnist_image = np.expand_dims(mnist_image, 0)

    return mnist_image, correct

def load_sample_weight():
    with open("mnist_weight.pkl", 'rb') as f:
        weight = pickle.load(f)
    
    return weight

def init_weight():
    input_size = 784
    layer2_size = 50
    layer3_size = 100
    output_size = 10

    weight_init=0.01
    weight = {}
    weight['W1'] = weight_init * np.random.randn(input_size, layer2_size)
    weight['W2'] = weight_init * np.random.randn(layer2_size, layer3_size)
    weight['W3'] = weight_init * np.random.randn(layer3_size, output_size)

    weight['b1'] = np.zeros(layer2_size)
    weight['b2'] = np.zeros(layer3_size)
    weight['b3'] = np.zeros(output_size)

    return weight

def forward(mnist_image, weight):
    W1, W2, W3 = weight['W1'], weight['W2'], weight['W3']
    b1, b2, b3 = weight['b1'], weight['b2'], weight['b3']

    # 1層目
    _y1 = np.dot(mnist_image, W1) + b1
    y1 = sigmoid(_y1)

    # 2層目
    _y2 = np.dot(y1, W2) + b2
    y2 = sigmoid(_y2)

    # 3層目
    _y3 = np.dot(y2, W3) + b3
    y3 = softmax(_y3)

    return _y1, _y2, _y3, y1, y2, y3

def sigmoid_gradient(x):
    gradient = (1.0 - sigmoid(x)) * sigmoid(x)
    return gradient


if __name__ == '__main__':

    mnist_image, correct = get_sample_mnist()
    #weight = load_sample_weight()
    weight = init_weight()

    # 推定
    _y1, _y2, _y3, y1, y2, y3 = forward(mnist_image, weight)

    predict = y3

    # 損失(誤差)計算
    loss = -np.sum(correct * np.log(predict + 1e-7))

    # 誤差の逆伝播
    W1, W2, W3 = weight['W1'], weight['W2'], weight['W3']
    b1, b2, b3 = weight['b1'], weight['b2'], weight['b3']

    gradiants = {} # 勾配
    dy3 = predict - correct
    gradiants['W3'] = np.dot(y2.T, dy3)
    gradiants['b3'] = np.sum(dy3, axis=0)
    
    dy2 = np.dot(dy3, W3.T)
    d_y2 = sigmoid_gradient(y2) * dy2
    gradiants['W2'] = np.dot(y1.T, d_y2)
    gradiants['b2'] = np.sum(d_y2, axis=0)

    dy1 = np.dot(dy2, W2.T)
    d_y1 = sigmoid_gradient(y1) * dy1
    gradiants['W1'] = np.dot(mnist_image.T, d_y1)
    gradiants['b1'] = np.sum(d_y1, axis=0)

    print(gradiants)

    # 重みの更新
    learning_rate = 0.1
    weight['W1'] -= learning_rate * gradiants['W1']
    weight['W2'] -= learning_rate * gradiants['W2']
    weight['W3'] -= learning_rate * gradiants['W3']
    weight['b1'] -= learning_rate * gradiants['b1']
    weight['b2'] -= learning_rate * gradiants['b2']
    weight['b3'] -= learning_rate * gradiants['b3']