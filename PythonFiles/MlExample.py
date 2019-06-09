# This is designed to show you what an actual codebase might look like. Don't be worried if it doesn't make sense. 
# This is a snippet of a machine learning program that should be able to detect spoken digits. 
# I'm adapting it to tell the difference between different beatbox sound gestures so that I can turn them into midi.
# To do that, I'll also need several other mechanisms including an onset detector for mapped sounds.

import tensorflow as tf 
from tensorflow import keras
import librosa
import os

import numpy as np 
import matplotlib.pyplot as plt 

# fashion_mnist = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class LearningRecording:
    def __init__(self, path):
        
        # defines self.path
        self.path = os.path.join(data_path, path)
        self.valid = False

        # print(self.path)
        # defines self.audio, self.label
        if (int(path[0]) in [0, 1, 2, 3, 4]) and (path[1] == '_'):
            self.audio, self.sr = librosa.load(self.path, mono=0, sr=22050)
            self.label = int(path[0])
        elif path[2] == '_':
            self.audio, self.sr = librosa.load(self.path, mono=0, sr=22050)
            self.label = int(path[0:2]) 
        elif int(path[0]) in [5, 6, 7, 8, 9]:
            self.audio, self.sr = librosa.load(self.path, mono=0, sr=22050)
            self.label = int(path[0])
        else: 
            print('loading failed on {}'.format(self.path))


        self.nsamples = len(self.audio)
        self.image = None


    def makeImage(self, maxNumSamp, spectSize=1024):
        if self.nsamples < maxNumSamp: # if the clip is shorter than the longest clip:
            # np.pad(self.audio, (0, maxNumSamp - self.nsamples), mode='constant', constant_values=(0.,0.))
            self.audio = np.append(self.audio, np.zeros((maxNumSamp - self.nsamples,)), axis = 0)
            # print('length: {}'.format(self.audio.shape))
        
        self.image = librosa.core.stft(self.audio, n_fft=spectSize, dtype=np.uint8)


data_path = '/Users/zt/data/recordings/'
data, valid = [], []    
maxlen = 0
class_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in os.listdir(data_path):
    a = LearningRecording(i)
    if a.nsamples > maxlen:
        maxlen = a.nsamples
    data.append(a)

print('maxlen: {}'.format(maxlen))
for i in data:
    i.makeImage(maxlen)
    

# makes validation set
for i, e in enumerate(data):
    if i % 13 == 0:
        e.valid = True
        valid.append(e)
        data.remove(e)

print('\ndata[0].image.shape: {}\n'.format(data[0].image.shape))

model = keras.Sequential([
    keras.layers.Flatten(input_shape=data[0].image.shape),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print([i.label for i in data])
data_images, data_labels = np.array([i.image for i in data]), np.array([i.label for i in data])
test_images, test_labels = np.array([i.image for i in valid]), np.array([i.label for i in valid])

print('data_images.shape: {}\ndata_labels.shape: {}'.format(data_images.shape, data_labels.shape)) 
print('test_images.shape: {}\ntest_labels.shape: {}'.format(test_images.shape, test_labels.shape))


model.fit(data_images, data_labels, epochs=50)

test_loss, test_acc = model.evaluate(test_images, test_labels)


predictions = model.predict(test_images)

# correct = 0
# incorrect = 0

# for i in range(len(predictions)):
#     if np.argmax(predictions[0]) == [k.label[0] for k in valid]:
#         correct += 1
#     else:
#         incorrect += 1

# print('correct {}; incorrect {}'.format(correct, incorrect))
# print('loss: {}; accuracy: {}'.format(test_loss, test_acc))