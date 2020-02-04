import tensorflow as tf


class Network:
    def __init__(self):
        self.learing_rate=0.001

        self.x=tf.placeholder(tf.float32,[None,784])

        self.label=tf.placeholder(tf.float32,[None,10])

        self.w=tf.Variable(tf.zeros([784,10]))

        self.b=tf.Variable(tf.zeros([10]))

        self.y=tf.nn.softmax(tf.matmul(self.x,self.w)+self.b)

        self.loss=-tf.reduce_sum(self.label*tf.log(self.y+1e-10))

        self.train=tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss)

        predict=tf.equal(tf.argmax(self.label,1), tf.argmax(self.y,1))

        self.accuracy=tf.reduce_mean(tf.cast(predict,"float"))
        

