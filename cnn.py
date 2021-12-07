from __future__ import print_function
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Conv2D, MaxPooling1D, Flatten, Dense, Activation, Dropout
from tensorflow.keras.layers import LeakyReLU


class CNN(object):
    def __init__(self):
        # change these to appropriate values
        self.batch_size = 64
        self.epochs = 7
        self.init_lr= 0.001 #learning rate

        # No need to modify these
        self.model = None

    def get_vars(self):
        return self.batch_size, self.epochs, self.init_lr

    def create_net(self):
        '''
        In this function you are going to build a convolutional neural network based on TF Keras.
        First, use Sequential() to set the inference features on this model. 
        Then, use model.add() to build layers in your own model
        Return: model
        '''
        self.model = Sequential()
        self.model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(32958, 3)))
        self.model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(MaxPooling1D(pool_size=2))
        self.model.add(Flatten())
        self.model.add(Dense(100, activation='relu'))
        self.model.add(Dense(32958, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return self.model
        #TODO: implement this
        # raise NotImplementedError

    def compile_net(self, model):
        '''
        In this function you are going to compile the model you've created.
        Use model.compile() to build your model.
        '''
        self.model = model
        self.model.compile(optimizer="Adam", loss="mse", metrics=[tf.keras.metrics.BinaryAccuracy(name = "accuracy")])

        #TODO: implement this
        # raise NotImplementedError

        return self.model