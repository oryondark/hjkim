import tensorflow as tf
def alex_net(images, classes, dropout):
    #Preprocess images & input layer
    resp_imgs = tf.reshape(images, shape=[-1, 256, 256, 3])

    # Convolution Layer-1
    conv1 = tf.layers.conv2d(resp_imgs, 64, 3, activation=tf.nn.relu)
    pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1])
    norm1 = tf.nn.lrn(pool1, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75)
    norm1 = tf.nn.dropout(norm1, dropout)

    # Convolution Layer-2
    conv2 = tf.layers.conv2d(norm1, 128, 3, activation=tf.nn.relu)
    pool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1])
    norm2 = tf.nn.lrn(pool2, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75)
    norm2 = tf.nn.dropout(norm2, dropout)

    # Convolution Layer-3
    conv3 = tf.layers.conv2d(norm2, 256, 5, activation=tf.nn.relu)
    pool3 = tf.nn.max_pool(conv3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1])
    norm3 = tf.nn.lrn(pool3, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75)
    norm3 = tf.nn.dropout(norm3, dropout)

    # Fully-connected layer for classification
    flatten = tf.layers.flatten(norm3)
    dense1 = tf.nn.relu(tf.layers.dense(flatten, 2048))
    dense2 = tf.nn.relu(tf.layers.dense(dense1, 1024))
    dense3 = tf.nn.relu(tf.layers.dense(dense2, 512))

    out = tf.layers.dense(dense3, classes)
    return out

