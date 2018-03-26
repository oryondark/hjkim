import numpy as np
import tensorflow as tf

import os
if os.environ.get('TensorFlow','AVX2') == 'AVX2':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


from sklearn.datasets import fetch_california_housing


def tensor_lesson_1():
    housing = fetch_california_housing()
    m, n = housing.data.shape

    housing_data_plus_bias = np.c_[np.ones((m,1)), housing.data]
    
    x = tf.constant(housing_data_plus_bias, dtype=tf.float32, name="x")
    y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name="y")
    xt = tf.transpose(x)
    print(x)
    print(y)
    print(xt)

    print(str(x*y))

    theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(xt, x)), xt), y)
    print(str(theta))
    try:
        print(str(theta.eval()))
    except Exception as tf_get_error:
        with tf.Session() as sess:
            print(tf_get_error)
            theta_value = theta.eval()
            print(str(theta_value))

if __name__=="__main__":
    #start to tensor_main.
    tensor_lesson_1()

