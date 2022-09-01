# coding: utf-8
# Written by K. Takano

import pickle
import numpy as np


mnist_file = "mnist.pkl"
NUM_CLASSES = 10

def load_mnist():
    with open(mnist_file, 'rb') as f:
        mnist = pickle.load(f)

    return (mnist['train_image'], mnist['train_label']), (mnist['test_image'], mnist['test_label'])

def to_one_hot_label(_label):
    one_hot_label = np.zeros((_label.size, NUM_CLASSES))
    for idx, row in enumerate(one_hot_label):
        row[_label[idx]] = 1
    return one_hot_label

from PIL import Image
def show_mnist(mnist_img):
    img = Image.fromarray(np.uint8(mnist_img))
    img.show()

def save_mnist(mnist_img):
    img = Image.fromarray(np.uint8(mnist_img))
    img.save("mnist.png")

if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist()

    mnist_img = x_train[0]
    mnist_label = t_train[0]

    mnist_img = mnist_img.astype(np.float32)
    mnist_img = mnist_img.reshape(28, 28) 
    print(mnist_label)
    show_mnist(mnist_img)
    save_mnist(mnist_img)



