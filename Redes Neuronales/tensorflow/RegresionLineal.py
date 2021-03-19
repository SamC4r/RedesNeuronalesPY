import tensorflow as tf
import numpy as np
#import matplotlib as plt
'''
function: create a linear model which try to fit the line
 y = x + 2 using SGD optimizer to minimize
 root-mean-square(RMS) loss function
'''
num_epoch = 100

x = np.linspace(-5,5,100)
fx = x+2

plt.hist(fx,[-10,10])

x = np.array([0.,1.,2.,3.],dtype=np.float32)
y = np.array([2.,3.,4.,5.],dtype=np.float32)

x = np.reshape(x,[4,1])
y = np.reshape(y,[4,1])
x_test = x+0.5
y_test = y+0.5

# This part of the script builds the TensorFlow graph using the Python API
# First declare placeholders for input x and label y
# Placeholders are TensorFlow variables requiring to be explicitly fed by some
# input data

x_ph = tf.placeholder(tf.float32, shape=[None, 1])
y_ph = tf.placeholder(tf.float32, shape=[None, 1])

# Variables (if not specified) will be learnt as the GradientDescentOptimizer

# is run
# Declare weight variable initialized using a truncated_normal law
W = tf.Variable(tf.truncated_normal([1, 1], stddev=0.1))
# Declare bias variable initialized to a constant 0.1
b = tf.Variable(tf.constant(0.1, shape=[1]))
# Initialize variables just declared
init = tf.initialize_all_variables()
# In this part of the script, we build operators storing operations
# on the previous variables and placeholders.
# model: y = w * x + b
y_pred = x_ph * W + b
# loss function
loss = tf.mul(tf.reduce_mean(tf.square(tf.sub(y_pred, y_ph))), 1. / 2)
# create training graph
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# This part of the script runs the TensorFlow graph (variables and operations
# operators) just built.
with tf.Session() as sess:
 	# initialize all the variables by running the initializer operator
 	sess.run(init)
 	for epoch in xrange(num_epoch):
		# Run sequentially the train_op and loss operators with
		# x_ph and y_ph placeholders fed by variables x and y

		loss_val = sess.run([train_op, loss], feed_dict={x_ph:x,y_ph:y})
		print('time:  %d: loss is %.4f' % (epoch, loss_val))

		# see what model do in the test set
		# by evaluating the y_pred operator using the x_test data
	test_val = sess.run(y_pred, feed_dict={x_ph: x_test})
	print('ground truth y is: %s' % y_test.flatten())
	print('predict y is : %s' % test_val.flatten())
