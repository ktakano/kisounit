# coding: utf-8
# Written by K. Takano
import numpy as np

def cross_entropy_loss(predict, correct, batch_size=1):
    loss = -np.sum(correct * np.log(predict + 1e-7)) / batch_size

    return loss

if __name__ == '__main__':
    correct = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, ])
    predict = np.array([0.1, 0.1, 0.0, 0.15, 0.7, 0.0, 0.05, 0.0, 0.0, 0.0])

    loss = cross_entropy_loss(predict, correct)

    print(loss)