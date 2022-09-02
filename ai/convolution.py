# coding: utf-8
# Written by K. Takano

import numpy as np
from mnist import load_mnist


(x_train, t_train), (x_test, t_test) = load_mnist()
x_train = x_train.astype(np.float32)