import numpy as np
import tensorflow as tf

def custom_init(shape, dtype=tf.float32, partition_info=None, seed=0):
    return tf.random_normal(shape, dtype=dtype, seed=seed)

def conv_1x1(x, num_outputs):
    kernel_size = 1
    stride      = 1
    return tf.layers.conv2d(x, num_outputs, kernel_size, stride, kernel_initializer=custom_init)

num_outputs = 2
x           = tf.constant(np.random.randn(1, 2, 2, 1), dtype=tf.float32)
dense_out   = tf.layers.dense(x, num_outputs, kernel_initializer=custom_init)
conv_out    = conv_1x1(x, num_outputs)
    
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    a = sess.run(dense_out)
    b = sess.run(conv_out)
    print("Dense Output =", a)
    print("Conv 1x1 Output =", b)

    print("Same output? =", np.allclose(a, b, atol=1.e-5))

