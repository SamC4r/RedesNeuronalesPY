import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

def run_cnn():
	mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
	tasaAprende = 0.001
	epochs = 10
	batch_size = 50
	x = tf.placeholder(tf.float32,[None,784])
	x_shaped = tf.reshape(x,[-1,28,28,1])
	y = tf.placeholder(tf.float32,[None, 10])
	layer1 = create_new_conv_layer(x_shaped, 1, 32, [5, 5], [2, 2], name='layer1')
 	layer2 = create_new_conv_layer(layer1, 32, 64, [5, 5], [2, 2], name='layer2')
 	flattened = tf.reshape(layer2, [-1, 7 * 7 * 64])
 	wd1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1000], stddev=0.03),name='wd1')
 	bd1 = tf.Variable(tf.truncated_normal([1000], stddev=0.01), name='bd1')
 	dense_layer1 = tf.matmul(flattened, wd1) + bd1
 	dense_layer1 = tf.nn.relu(dense_layer1)
 	wd2 = tf.Variable(tf.truncated_normal([1000, 10], stddev=0.03), name='wd2')
 	bd2 = tf.Variable(tf.truncated_normal([10], stddev=0.01), name='bd2')
 	dense_layer2 = tf.matmul(dense_layer1, wd2) + bd2
 	y_ = tf.nn.softmax(dense_layer2)
 	cross_entropy =
	tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=dense_layer2,labels=y))
 	optimiser = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cross_entropy)
 	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
 	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
 	init_op = tf.global_variables_initializer()

 	tf.summary.scalar('accuracy', accuracy)
 	merged = tf.summary.merge_all()
 	writer = tf.summary.FileWriter('E:\TensorFlowProject')
 	with tf.Session() as sess:
 		sess.run(init_op)
 		total_batch = int(len(mnist.train.labels) / batch_size)
 		for epoch in range(epochs):
 			avg_cost = 0
 			for i in range(total_batch):
 				batch_x, batch_y = mnist.train.next_batch(batch_size=batch_size) _, c = sess.run([optimiser, cross_entropy], feed_dict={x:
batch_x, y: batch_y})
 avg_cost += c / total_batch
 test_acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y:
mnist.test.labels})
 summary = sess.run(merged, feed_dict={x: mnist.test.images, y:
mnist.test.labels})
 writer.add_summary(summary, epoch)
 print("\nTraining complete!")
 writer.add_graph(sess.graph)
 print(sess.run(accuracy, feed_dict={x: mnist.test.images, y:
mnist.test.labels}))
def create_new_conv_layer(input_data, num_input_channels, num_filters,
filter_shape, pool_shape, name):
 conv_filt_shape = [filter_shape[0], filter_shape[1], num_input_channels,
num_filters]
 weights = tf.Variable(tf.truncated_normal(conv_filt_shape, stddev=0.03),
name=name+'_W')
 bias = tf.Variable(tf.truncated_normal([num_filters]), name=name+'_b')
#Out layer defines the output
 out_layer =
tf.nn.conv2d(input_data, weights, [1, 1, 1, 1], padding='SAME')
 out_layer += bias



run_cnn()